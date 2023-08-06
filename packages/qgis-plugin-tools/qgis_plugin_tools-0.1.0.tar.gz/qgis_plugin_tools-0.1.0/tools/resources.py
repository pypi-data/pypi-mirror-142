"""Tools to work with resource files."""

import configparser
from os.path import abspath, dirname, exists, join, pardir
from pathlib import Path
from typing import Dict, Optional

from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QDialog, QWidget

__copyright__ = "Copyright 2019, 3Liz, 2020-2021 Gispo Ltd"
__license__ = "GPL version 3"
__email__ = "info@3liz.org"
__revision__ = "$Format:%H$"

from qgis.core import QgsApplication

PLUGIN_NAME: str = ""
SLUG_NAME: str = ""


def plugin_path(*args: str) -> str:
    """Get the path to plugin root folder.

    :param args List of path elements e.g. ['img', 'logos', 'image.png']
    :type args: str

    :return: Absolute path to the resource.
    :rtype: str
    """
    path = dirname(dirname(__file__))
    path = abspath(abspath(join(path, pardir)))
    for item in args:
        path = abspath(join(path, item))

    return path


def root_path(*args: str) -> str:
    """Get the path to plugin root folder.

    :param args List of path elements e.g. ['img', 'logos', 'image.png']
    :type args: str

    :return: Absolute path to the resource.
    :rtype: str
    """
    path = dirname(dirname(__file__))
    path = abspath(abspath(join(path, pardir, pardir)))
    for item in args:
        path = abspath(join(path, item))

    return path


def profile_path(*args: str) -> str:
    """
    Get the path inside profile folder.
    return: Absolute path to the resource.
    """
    path = QgsApplication.qgisSettingsDirPath()
    for item in args:
        path = abspath(join(path, item))

    return path


def plugin_name() -> str:
    """Return the plugin name according to metadata.txt.

    :return: The plugin name.
    :rtype: basestring
    """
    global PLUGIN_NAME
    if PLUGIN_NAME == "":
        try:
            metadata = metadata_config()
            name: str = metadata["general"]["name"]
            name = name.replace(" ", "").strip()
            PLUGIN_NAME = name
        except KeyError:
            PLUGIN_NAME = "test_plugin"
    return PLUGIN_NAME


def slug_name() -> str:
    """Return project slug name in .qgis-plugin.ci"""
    global SLUG_NAME
    if SLUG_NAME == "":
        try:
            metadata = metadata_config()
            name: str = metadata["general"]["repository"]
            slug = name.split("/")[-1]
            SLUG_NAME = slug
        except KeyError:
            SLUG_NAME = PLUGIN_NAME
    return SLUG_NAME


def task_logger_name() -> str:
    """
    Returns the name for task logger
    """
    return f"{plugin_name()}_task"


def metadata_config() -> configparser.ConfigParser:
    """Get the INI config parser for the metadata file.

    :return: The config parser object.
    :rtype: ConfigParser
    """
    path = plugin_path("metadata.txt")
    config = configparser.ConfigParser()
    config.read(path)
    return config


def qgis_plugin_ci_config() -> Optional[Dict]:
    """
    Get configuration of the ci config or None
    """
    path_str = root_path(".qgis-plugin-ci")
    if not Path(path_str).exists():
        path_str = plugin_path(".qgis-plugin-ci")
    path = Path(path_str)
    if path.exists():
        with open(path) as f:
            config = {}
            for line in f:
                parts = line.split(":")
                config[parts[0]] = ":".join(parts[1:])

        return config
    return None


def plugin_test_data_path(*args: str) -> str:
    """Get the path to the plugin test data path.

    :param args List of path elements e.g. ['img', 'logos', 'image.png']
    :type args: str

    :return: Absolute path to the resources folder.
    :rtype: str
    """

    path = abspath(abspath(join(root_path(), "test", "data")))
    if not exists(path):
        path = abspath(abspath(join(plugin_path(), "test", "data")))
    for item in args:
        path = abspath(join(path, item))

    return path


def resources_path(*args: str) -> str:
    """Get the path to our resources folder.

    :param args List of path elements e.g. ['img', 'logos', 'image.png']
    :type args: str

    :return: Absolute path to the resources folder.
    :rtype: str
    """
    path = abspath(abspath(join(plugin_path(), "resources")))
    for item in args:
        path = abspath(join(path, item))

    return path


def qgis_plugin_tools_resources(*args: str) -> str:
    """Get the path within the qgis_plugin_tools submodule"""
    return str(Path(__file__, "..", "..", "resources", *args).resolve().absolute())


def load_ui(*args: str) -> QWidget:
    """Get compiled UI file.

    :param args List of path elements e.g. ['img', 'logos', 'image.png']
    :type args: str

    :return: Compiled UI file.
    """
    ui_class, _ = uic.loadUiType(resources_path("ui", *args))
    return ui_class


def ui_file_dialog(*ui_file_name_parts: str):  # noqa ANN201
    """DRY helper for building classes from a .ui file"""

    class UiFileDialogClass(QDialog, load_ui(*ui_file_name_parts)):  # type: ignore
        def __init__(
            self,
            parent: Optional[QWidget],
        ) -> None:
            super().__init__(parent)
            self.setupUi(self)  # provided by load_ui FORM_CLASS

    return UiFileDialogClass
