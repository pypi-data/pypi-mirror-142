from pathlib import Path

import pytest
import astropy.units as u
from astropy.modeling import Model

from dkist.conftest import *
from dkist_inventory.asdf_generator import headers_from_filenames
from dkist_inventory.transforms import TransformBuilder

from dkist_data_simulator.spec214.vtf import SimpleVTFDataset
from dkist_data_simulator.spec214.visp import SimpleVISPDataset, TimeDependentVISPDataset
from dkist_data_simulator.spec214.vbi import MosaicedVBIBlueDataset, TimeDependentVBIDataset


def rm_tree(pth):
    for child in pth.glob('*'):
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    pth.rmdir()


@pytest.fixture(scope="session", params=[
    "vtf",
    "visp",
    "vbi-mosaic",
    "vbi-time-varying",
    # "visp-time-varying",
])
def header_directory(request, tmpdir_factory):
    if "time-varying" in request.param and not hasattr(Model, "_calculate_separability_matrix"):
        pytest.skip()

    atmpdir = Path(tmpdir_factory.mktemp(request.param))

    datasets = {
        "visp": SimpleVISPDataset(2, 2, 4, 5, linewave=500 * u.nm),
        "vtf": SimpleVTFDataset(2, 2, 4, 5, linewave=500 * u.nm),
        "vbi-mosaic": MosaicedVBIBlueDataset(n_time=2, time_delta=10, linewave=400 * u.nm),
        "vbi-time-varying": TimeDependentVBIDataset(n_time=4, time_delta=10, linewave=400 * u.nm,
                                                    detector_shape=(1024, 1024)),
        "visp-time-varying": TimeDependentVISPDataset(3, 4, 1, 10, linewave=500 * u.nm,
                                                      detector_shape=(1024, 1024)),
    }

    ds = datasets[request.param]
    ds.generate_files(atmpdir, f"{request.param.upper()}_{{ds.index}}.fits")

    yield atmpdir

    # Cleanup at the end of the session
    rm_tree(atmpdir)


@pytest.fixture
def vbi_time_varying_transform_builder(header_directory):
    if "vbi-time-varying" not in header_directory.as_posix():
        pytest.skip()

    headers = headers_from_filenames(header_directory.glob("*"))
    return TransformBuilder(headers)


@pytest.fixture
def header_filenames(header_directory):
    files = list(header_directory.glob("*"))
    files.sort()
    return files


@pytest.fixture
def transform_builder(header_filenames):
    # We can't build a single transform builder for a mosaic
    if "vbi-mosaic" in header_filenames[0].as_posix():
        pytest.skip()
    headers = headers_from_filenames(header_filenames)
    return TransformBuilder(headers)
