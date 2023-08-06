# type: ignore
# flake8: noqa ANN201

__copyright__ = "Copyright 2020-2021, Gispo Ltd"
__license__ = "GPL version 3"
__email__ = "info@gispo.fi"
__revision__ = "$Format:%H$"

import pytest

from ..testing.utilities import TestTaskRunner
from ..tools.custom_logging import setup_logger, teardown_logger
from ..tools.resources import plugin_name


@pytest.fixture(scope="session")
def initialize_logger(qgis_iface):
    setup_logger(plugin_name(), qgis_iface)


@pytest.fixture()
def task_runner(initialize_logger):
    return TestTaskRunner()
