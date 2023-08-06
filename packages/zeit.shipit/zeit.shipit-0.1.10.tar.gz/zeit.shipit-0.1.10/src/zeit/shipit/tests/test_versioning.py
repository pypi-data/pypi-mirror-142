from os import path
import pytest
from zeit.shipit import Package, utils


@pytest.fixture(scope="session")
def asset_path():
    def getter(*parts):
        return path.abspath(path.join(path.dirname(__file__), *parts))

    return getter


@pytest.fixture()
def mypackage(asset_path):
    return Package("mypackage", asset_path("mypackage"))


def test_read_release_version(mypackage):
    assert mypackage.release_version == "1.2.3dev"


def test_read_deployment_version(mypackage):
    assert mypackage.deployment_version == "1.2.2"


@pytest.mark.parametrize("old,new", [("1.2.2", "1.2.3dev"), ("3", "4dev"), ("1.9", "1.10dev")])
def test_bump_version(old, new):
    assert utils.bump_version(old) == new
