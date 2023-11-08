from __future__ import annotations

import os
import shutil
from pathlib import Path
from typing import Any

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


def pytest_report_header(config: dict[str, Any]) -> str:
    header = "libraries: Sphinx-{}, docutils-{}".format(
        sphinx.__display_version__,
        docutils.__version__,
    )
    if hasattr(config, "_tmp_path_factory"):
        header += "\nbase tempdir: %s" % config._tmp_path_factory.getbasetemp()

    return header


def _initialize_test_directory(_session: pytest.Session) -> None:
    tempdir_str = os.getenv("SPHINX_TEST_TEMPDIR")
    if tempdir_str:
        tempdir = Path(tempdir_str).resolve()
        print("Temporary files will be placed in %s." % tempdir)

        if tempdir.exists():
            shutil.rmtree(tempdir)

        tempdir.mkdir(parents=True)


def pytest_sessionstart(session: pytest.Session) -> None:
    _initialize_test_directory(session)
