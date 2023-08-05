"""
Functionality relating to creating gWCS frames and Astropy models from SPEC 214 headers.
"""
import re
from collections import defaultdict
from functools import partial
from itertools import product

import astropy.modeling.models as m
import astropy.table
import astropy.units as u
import gwcs
import gwcs.coordinate_frames as cf
import numpy as np
from astropy.modeling import CompoundModel
from astropy.time import Time
from dkist.wcs.models import (VaryingCelestialTransform,
                              generate_celestial_transform, CoupledCompoundModel)
from sunpy.coordinates import Helioprojective

__all__ = [
    "TransformBuilder",
    "spectral_model_from_framewave",
    "time_model_from_date_obs",
    "generate_lookup_table",
    "linear_time_model",
    "linear_spectral_model",
    "spatial_model_from_header",
]


PRIMARY_WCS_CTYPE = re.compile(r"(CTYPE\d+$)")


def identify_spatial_axes(header):
    """
    Given a FITS WCS header identify which axis number is lat and which is lon.
    """
    latind = None
    lonind = None
    for k, v in header.items():
        key_is_not_primary_wcs_ctype = not bool(re.search(PRIMARY_WCS_CTYPE, k))
        if key_is_not_primary_wcs_ctype:
            continue
        if isinstance(v, str) and v.startswith("HPLN-"):
            lonind = int(k[5:])
        if isinstance(v, str) and v.startswith("HPLT-"):
            latind = int(k[5:])

    if latind is None or lonind is None:
        raise ValueError("Could not extract HPLN and HPLT from the header.")

    latalg = header[f"CTYPE{latind}"][5:]
    lonalg = header[f"CTYPE{lonind}"][5:]

    if latalg != lonalg:
        raise ValueError(
            "The projection of the two spatial axes did not match."
        )  # pragma: no cover

    return latind, lonind


def spatial_model_from_header(header):
    """
    Given a FITS compliant header with CTYPEx,y as HPLN, HPLT return a
    `~astropy.modeling.CompositeModel` for the transform.

    This function finds the HPLN and HPLT keys in the header and returns a
    model in Lon, Lat order.
    """
    latind, lonind = identify_spatial_axes(header)

    cunit1, cunit2 = u.Unit(header[f"CUNIT{lonind}"]), u.Unit(header[f"CUNIT{latind}"])
    crpix = (header[f"CRPIX{lonind}"], header[f"CRPIX{latind}"]) * u.pix
    crval = u.Quantity([header[f"CRVAL{lonind}"] * cunit1, header[f"CRVAL{latind}"] * cunit2])
    cdelt = u.Quantity([
        header[f"CDELT{lonind}"] * (cunit1 / u.pix),
        header[f"CDELT{latind}"] * (cunit2 / u.pix),
    ])
    pc = np.array([
        [header[f"PC{lonind}_{lonind}"], header[f"PC{lonind}_{latind}"]],
        [header[f"PC{latind}_{lonind}"], header[f"PC{latind}_{latind}"]],
    ]) * cunit1

    latproj = header[f"CTYPE{latind}"][5:]
    lonpole = header.get("LONPOLE")
    if not lonpole and latproj == "TAN":
        lonpole = 180

    if not lonpole:
        raise ValueError(f"LONPOLE not specified and not known for projection {latproj}")

    projections = {"TAN": m.Pix2Sky_TAN()}

    return (
        np.mean(cdelt).to_value(u.arcsec/u.pix),
        generate_celestial_transform(crpix, cdelt, pc, crval,
                                     lon_pole=lonpole, projection=projections[latproj])
    )


def varying_spatial_model_from_headers(headers: astropy.table.Table, varying_axes: dict[str, list[int]]):
    """
    Generate a varying celestial model from a set of headers.
    """
    if "pc" in varying_axes and "crval" in varying_axes:
        if varying_axes["pc"] != varying_axes["crval"]:
            raise ValueError(
                "Both the pointing and the rotation vary over different"
                " dimensions of the dataset. I don't know what to do here."
            )
        vaxes = varying_axes["crval"]
    elif "crval" in varying_axes:
        vaxes = varying_axes["crval"]
    elif "pc" in varying_axes:
        vaxes = varying_axes["pc"]
    else:
        raise ValueError("What is this varying_axes dict you have given me?!")

    header = dict(headers[0])
    latind, lonind = identify_spatial_axes(header)
    cunit1, cunit2 = u.Unit(header[f"CUNIT{lonind}"]), u.Unit(header[f"CUNIT{latind}"])
    crpix = (header[f"CRPIX{lonind}"], header[f"CRPIX{latind}"]) * u.pix
    cdelt = u.Quantity([
        header[f"CDELT{lonind}"] * (cunit1 / u.pix),
        header[f"CDELT{latind}"] * (cunit2 / u.pix),
    ])

    # Extract tables
    varying_shape = [header[f"DNAXIS{d}"] for d in vaxes]

    if "crval" in varying_axes:
        crval_table = headers[[f"CRVAL{i}" for i in (lonind, latind)]]
        # Coerce the astropy table to a regular float numpy array
        crval_table = crval_table.as_array().view((float, len(crval_table.columns)))
        crval_table = crval_table.reshape(varying_shape + [2])
        crval_table = crval_table << cunit1
    else:
        crval_table = u.Quantity(header[f"CRVAL{lonind}"] * cunit1, header[f"CRVAL{latind}"] * cunit2)

    if "pc" in varying_axes:
        pc_table = headers[[f"PC{i}_{j}" for i, j in product(*[(lonind, latind)]*2)]]
        # Coerce the astropy table to a regular float numpy array
        pc_table = pc_table.as_array().view((float, len(pc_table.columns)))
        pc_table = pc_table.reshape(varying_shape + [2, 2])
        pc_table = pc_table << cunit1
    else:
        pc_table = np.array([
            [header[f"PC{lonind}_{lonind}"], header[f"PC{lonind}_{latind}"]],
            [header[f"PC{latind}_{lonind}"], header[f"PC{latind}_{latind}"]],
        ]) * cunit1

    vct = VaryingCelestialTransform(cdelt=cdelt, crpix=crpix, crval_table=crval_table, pc_table=pc_table)

    # TODO: estimate the spatial sampling somehow?
    return 0, vct


@u.quantity_input
def linear_spectral_model(spectral_width: u.nm, reference_val: u.nm):
    """
    Linear model in a spectral dimension. The reference pixel is always 0.
    """
    return m.Linear1D(slope=spectral_width / (1 * u.pix), intercept=reference_val)


@u.quantity_input
def linear_time_model(cadence: u.s, reference_val: u.s = 0 * u.s):
    """
    Linear model in a temporal dimension. The reference pixel is always 0.
    """
    if reference_val is None:
        reference_val = 0 * cadence.unit
    return m.Linear1D(slope=cadence / (1 * u.pix), intercept=reference_val)


def generate_lookup_table(lookup_table, interpolation="linear", points_unit=u.pix, **kwargs):
    if not isinstance(lookup_table, u.Quantity):
        raise TypeError("lookup_table must be a Quantity.")

    # The integer location is at the centre of the pixel.
    points = (np.arange(lookup_table.size) - 0) * points_unit

    kwargs = {"bounds_error": False, "fill_value": np.nan, "method": interpolation, **kwargs}

    return m.Tabular1D(points, lookup_table, **kwargs)


def time_model_from_date_obs(date_obs, date_beg=None):
    """
    Return a time model that best fits a list of dateobs's.
    """
    if not date_beg:
        date_beg = date_obs[0]
    date_obs = Time(date_obs)
    date_beg = Time(date_beg)

    deltas = date_obs - date_beg

    # Work out if we have a uniform delta (i.e. a linear model)
    ddelta = deltas.to(u.s)[1:] - deltas.to(u.s)[:-1]

    # If the length of the axis is one, then return a very simple model
    if ddelta.size == 0:
        raise ValueError("Why do you have a temporal axis in the DTYPEn keys if you only have a len 1 time axis?")
    elif u.allclose(ddelta[0], ddelta):
        slope = ddelta[0]
        intercept = 0 * u.s
        return slope.to_value(u.s), linear_time_model(cadence=slope, reference_val=intercept)
    else:
        print(f"Creating tabular temporal axis. ddeltas: {ddelta}")
        return np.mean(deltas).to_value(u.s), generate_lookup_table(deltas.to(u.s))


def spectral_model_from_framewave(framewav):
    """
    Construct a linear or lookup table model for wavelength based on the
    framewav keys.
    """
    framewav = u.Quantity(framewav, unit=u.nm)
    wave_beg = framewav[0]

    deltas = wave_beg - framewav
    ddeltas = deltas[:-1] - deltas[1:]
    # If the length of the axis is one, then return a very simple model
    if ddeltas.size == 0:
        raise ValueError("Why do you have a spectral axis in the DTYPEn keys if you only have a len 1 spectral axis?")
    if u.allclose(ddeltas[0], ddeltas):
        slope = ddeltas[0]
        return slope.to_value(u.nm), linear_spectral_model(slope, wave_beg)
    else:
        print(f"creating tabular wavelength axis. ddeltas: {ddeltas}")
        return np.mean(ddeltas).to_value(u.nm), generate_lookup_table(framewav)


class TransformBuilder:
    """
    This class builds compound models and frames in order when given axes types.
    """
    def __init__(self, headers: astropy.table.Table):
        if not isinstance(headers, astropy.table.Table):
            raise TypeError("headers should be an astropy table")
        self.header = dict(headers[0])

        # Reshape the headers to match the Dataset shape, so we can extract headers along various axes.
        shape = tuple(
            self.header[f"DNAXIS{n}"]
            for n in range(self.header["DNAXIS"], self.header["DAAXES"], -1)
        )
        arr_headers = np.empty(shape, dtype=object)
        for i in range(arr_headers.size):
            arr_headers.flat[i] = dict(headers[i])

        self.pixel_shape = tuple(
            self.header[f"DNAXIS{n}"] for n in range(1, self.header["DNAXIS"] + 1)
        )

        self.headers = arr_headers
        self.header_table = headers
        self.reset()
        self._build()

        self.spectral_sampling = None
        self.spatial_sampling = None
        self.temporal_sampling = None

    @property
    def pixel_frame(self):
        """
        A `gwcs.coordinate_frames.CoordinateFrame` object describing the pixel frame.
        """
        return cf.CoordinateFrame(
            naxes=self.header["DNAXIS"],
            axes_type=self.axes_types,
            axes_order=range(self.header["DNAXIS"]),
            unit=[u.pixel] * self.header["DNAXIS"],
            axes_names=[self.header[f"DPNAME{n}"] for n in range(1, self.header["DNAXIS"] + 1)],
            name="pixel",
        )

    @property
    def gwcs(self):
        """
        `gwcs.WCS` object representing these headers.
        """
        world_frame = cf.CompositeFrame(self.frames)

        out_wcs = gwcs.WCS(
            forward_transform=self.transform, input_frame=self.pixel_frame, output_frame=world_frame
        )
        out_wcs.pixel_shape = self.pixel_shape
        out_wcs.array_shape = self.pixel_shape[::-1]

        return out_wcs

    @property
    def frames(self):
        """
        The coordinate frames, in Python order.
        """
        return self._frames

    @property
    def transform(self):
        """
        Return the compound model.
        """
        # self._transforms is a tuple of (model, callable(left)).
        # The callable returns a CompoundModel instance when the right hand
        # side of the operator is passed.
        # We iterate backwards through the models generating the model for the
        # right hand side of the next step up the tree (i.e. from the inner
        # most operator to the outermost). So we start with the last model
        # instance (ignoring the callable), then pass that model to the next
        # callable as the right hand side, and continue to work our way back up
        # the tree.
        right, _ = self._transforms[-1]
        for _, func in self._transforms[:-1][::-1]:
            right = func(right=right)
        return right

    """
    Internal Stuff
    """

    @staticmethod
    def _compound_model_partial(left, op="&"):
        return partial(CompoundModel, left=left, op=op)

    def _build(self):
        """
        Build the state of the thing.
        """
        type_map = {
            "STOKES": self.make_stokes,
            "TEMPORAL": self.make_temporal,
            "SPECTRAL": self.make_spectral,
            "SPATIAL": self.make_spatial,
        }

        xx = 0
        while self._i < self.header["DNAXIS"]:  # < because FITS is i+1
            atype = self.axes_types[self._i]
            type_map[atype]()
            xx += 1
            if xx > 100:
                raise ValueError("Infinite loop in header parsing")  # pragma: no cover

    @property
    def axes_types(self):
        """
        The list of DTYPEn for the first header.
        """
        return [self.header[f"DTYPE{n}"] for n in range(1, self.header["DNAXIS"] + 1)]

    def reset(self):
        """
        Reset the builder.
        """
        self._i = 0
        self._frames = []
        self._transforms = []

    @property
    def n(self):
        """
        The FITS index of the current dimension.
        """
        return self._n(self._i)

    def _n(self, i):
        """
        Convert a Python index ``i`` to a FITS order index for keywords ``n``.
        """
        # return range(self.header['DNAXIS'], 0, -1)[i]
        return i + 1

    @property
    def slice_for_n(self):
        i = self._i - self.header["DAAXES"]
        naxes = self.header["DEAXES"]
        ss = [0] * naxes
        ss[i] = slice(None)
        return ss[::-1]

    @property
    def slice_headers(self):
        return self.headers[tuple(self.slice_for_n)]

    def get_units(self, *iargs):
        """
        Get zee units
        """
        u = [self.header.get(f"DUNIT{self._n(i)}", None) for i in iargs]

        return u

    def make_stokes(self):
        """
        Add a stokes axes to the builder.
        """
        name = self.header[f"DWNAME{self.n}"]
        self._frames.append(cf.StokesFrame(axes_order=(self._i,), name=name))
        transform = generate_lookup_table([0, 1, 2, 3] * u.one, interpolation="nearest")
        self._transforms.append((
            transform,
            self._compound_model_partial(left=transform))
        )
        self._i += 1

    def make_temporal(self):
        """
        Add a temporal axes to the builder.
        """

        name = self.header[f"DWNAME{self.n}"]
        self._frames.append(
            cf.TemporalFrame(
                axes_order=(self._i,),
                name=name,
                axes_names=(name,),
                unit=self.get_units(self._i),
                reference_frame=Time(self.header["DATE-BEG"]),
            )
        )
        self.temporal_sampling, transform = time_model_from_date_obs([e["DATE-BEG"] for e in self.slice_headers])
        self._transforms.append((transform, self._compound_model_partial(left=transform)))

        self._i += 1

    @staticmethod
    def constant_columns(table: astropy.table.Table, keys: list[str]):
        """
        Returns true if all columns given by keys have a constant value in table.
        """
        return all([np.allclose(table[0][k], table[k]) for k in keys])

    def get_varying_spatial_axes(self) -> dict[str, list[int]]:
        """
        Compute the axes over which CRVAL or PC vary.
        """
        NAXIS, DAAXES, DNAXIS = self.header["NAXIS"], self.header["DAAXES"], self.header["DNAXIS"]
        # Find which dataset axes the pointing varies along
        # If any of these keys vary along any of the dataset axes we want to know
        naxis_v = list(range(1, NAXIS + 1))
        crval_keys = [f"CRVAL{n}" for n in naxis_v]
        pc_keys = [f"PC{i}_{j}" for i, j in product(naxis_v, naxis_v)]
        varying_axes = defaultdict(list)
        for daxis in range(DAAXES + 1, DNAXIS + 1):
            key = f"DINDEX{daxis}"
            group = self.header_table.group_by(key)
            groups = group.groups if len(group.groups) < len(self.header_table) else [self.header_table]
            if all([not self.constant_columns(g, pc_keys) for g in groups]):
                varying_axes["pc"].append(daxis)
            if all([not self.constant_columns(g, crval_keys) for g in groups]):
                varying_axes["crval"].append(daxis)

        return dict(varying_axes)

    def make_spatial(self):
        """
        Add a helioprojective spatial pair to the builder.

        .. note::
            This increments the counter by two.

        """
        i = self._i
        name = self.header[f"DWNAME{self.n}"]
        name = name.split(" ")[0]
        axes_names = [
            self.header[f"DWNAME{nn}"] for nn in (self.n, self._n(i + 1))
        ]

        obstime = Time(self.header["DATE-AVG"])
        axes_types = [
            "lat" if "LT" in self.axes_types[i] else "lon",
            "lon" if "LN" in self.axes_types[i] else "lat",
        ]
        self._frames.append(
            cf.CelestialFrame(
                axes_order=(i, i + 1),
                name=name,
                # TODO: the celestial frame is wrong, we need to account for varying position and obstime
                reference_frame=Helioprojective(obstime=obstime),
                axes_names=axes_names,
                unit=self.get_units(self._i, self._i + 1),
                axis_physical_types=(
                    f"custom:pos.helioprojective.{axes_types[0]}",
                    f"custom:pos.helioprojective.{axes_types[1]}",
                ),
            )
        )

        varying_spatial_axes = self.get_varying_spatial_axes()
        if varying_spatial_axes:
            self.spatial_sampling, transform = varying_spatial_model_from_headers(self.header_table,
                                                                                  varying_spatial_axes)

            # At this point we have already verified that if there are both pc and
            # crval keys in this dict they are the same length, so just use the
            # first one.
            shared_inputs = len(list(varying_spatial_axes.values())[0])
            self._transforms.append((transform, partial(CoupledCompoundModel, op="&",
                                                        left=transform, shared_inputs=shared_inputs)))

        else:
            self.spatial_sampling, transform = spatial_model_from_header(self.header)
            self._transforms.append((transform, self._compound_model_partial(left=transform)))

        self._i += 2

    def make_spectral(self):
        """
        Decide how to make a spectral axes.
        """
        name = self.header[f"DWNAME{self.n}"]
        self._frames.append(
            cf.SpectralFrame(
                axes_order=(self._i,), axes_names=(name,), unit=self.get_units(self._i), name=name
            )
        )

        if "WAV" in self.header.get(f"CTYPE{self.n}", ""):  # Matches AWAV and WAVE
            self.spectral_sampling, transform = self.make_spectral_from_wcs()
        elif "FRAMEWAV" in self.header.keys():
            self.spectral_sampling, transform = self.make_spectral_from_dataset()
        else:
            raise ValueError(
                "Could not parse spectral WCS information from this header."
            )  # pragma: no cover

        self._transforms.append((transform, self._compound_model_partial(left=transform)))

        self._i += 1

    def make_spectral_from_dataset(self):
        """
        Make a spectral axes from (VTF) dataset info.
        """
        framewave = [h["FRAMEWAV"] for h in self.slice_headers[: self.header[f"DNAXIS{self.n}"]]]
        return spectral_model_from_framewave(framewave)

    def make_spectral_from_wcs(self):
        """
        Add a spectral axes from the FITS-WCS keywords.
        """
        spectral_cdelt = self.header[f"CDELT{self.n}"] * u.nm
        return spectral_cdelt, linear_spectral_model(
            spectral_cdelt, self.header[f"CRVAL{self.n}"] * u.nm
        )
