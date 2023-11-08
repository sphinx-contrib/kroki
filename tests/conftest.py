import os
import shutil
from pathlib import Path

import docutils
import pytest
import sphinx
from sphinx.testing.path import path

pytest_plugins = "sphinx.testing.fixtures"

# Exclude 'fixtures' dirs for pytest test collector
collect_ignore = ["fixtures"]


@pytest.fixture(scope="session")
def rootdir() -> path:
    return path(__file__).parent.abspath() / "fixtures"


def pytest_report_header(config) -> str:
    header = "libraries: Sphinx-{}, docutils-{}".format(
        sphinx.__display_version__,
        docutils.__version__,
    )
    if hasattr(config, "_tmp_path_factory"):
        header += "\nbase tempdir: %s" % config._tmp_path_factory.getbasetemp()

    return header


def _initialize_test_directory(_session: pytest.Session) -> None:
    if "SPHINX_TEST_TEMPDIR" in os.environ:
        tempdir = Path.resolve(os.getenv("SPHINX_TEST_TEMPDIR"))
        print("Temporary files will be placed in %s." % tempdir)

        if tempdir.exists():
            shutil.rmtree(tempdir)

        tempdir.mkdir(parents=True)


def pytest_sessionstart(session: pytest.Session) -> None:
    _initialize_test_directory(session)
