"""Setting up logging using QGIS, file, Sentry..."""

import logging
import warnings
from enum import Enum, unique
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any, Dict, Optional

from qgis.core import Qgis, QgsMessageLog
from qgis.gui import QgisInterface, QgsMessageBar
from qgis.PyQt.QtWidgets import QLayout, QVBoxLayout, QWidget

from .i18n import tr
from .resources import plugin_name, plugin_path, profile_path
from .settings import get_setting, setting_key

PLUGIN_NAME = plugin_name()

__copyright__ = "Copyright 2020-2021, Gispo Ltd"
__license__ = "GPL version 3"
__email__ = "info@gispo.fi"
__revision__ = "$Format:%H$"


@unique
class LogTarget(Enum):
    """Log target with default logging level as value"""

    STREAM = {"id": "stream", "default": "INFO"}
    FILE = {"id": "file", "default": "INFO"}
    BAR = {"id": "bar", "default": "INFO"}

    @property
    def id(self) -> str:
        return self.value["id"]

    @property
    def default_level(self) -> str:
        return self.value["default"]


def qgis_level(logging_level: str) -> int:
    """Check for the corresponding QGIS Level according to Logging Level.

    For QGIS:
    https://qgis.org/api/classQgis.html#a60c079f4d8b7c479498be3d42ec96257

    For Logging:
    https://docs.python.org/3/library/logging.html#levels

    :param logging_level: The Logging level
    :target logging_level: basestring

    :return: The QGIS Level
    :rtype: Qgis.MessageLevel
    """
    if logging_level == "CRITICAL":
        return Qgis.Critical
    elif logging_level == "ERROR":
        return Qgis.Critical
    elif logging_level == "WARNING":
        return Qgis.Warning
    elif logging_level == "INFO":
        return Qgis.Info
    elif logging_level == "DEBUG":
        return Qgis.Info

    return Qgis.Info


def bar_msg(
    details: Any = "", duration: Optional[int] = None, success: bool = False
) -> Dict[str, Any]:
    """
    Helper function to construct extra arguments for message bar logger message

    :param details: Longer body of the message. Can be set to empty string.
    :param duration: can be used to specify the message timeout in seconds. If
        ``duration`` is set to 0, then the message must be manually dismissed
        by the user.
    :param success: Whether the message is success message or not
    """
    args = {"details": str(details), "success": success}
    if duration is not None:
        args["duration"] = duration
    return args


class QgsLogHandler(logging.Handler):
    """A logging handler that will log messages to the QGIS logging console"""

    def __init__(self, level: int = logging.NOTSET) -> None:
        logging.Handler.__init__(self)

    def emit(self, record: logging.LogRecord) -> None:
        """Try to log the message to QGIS if available, otherwise do nothing.

        :param record: logging record containing whatever info needs to be
                logged.
        """
        try:
            # noinspection PyCallByClass,PyTypeChecker
            QgsMessageLog.logMessage(
                record.getMessage(), PLUGIN_NAME, qgis_level(record.levelname)
            )
        except MemoryError:
            message = tr(
                "Due to memory limitations on this machine, the plugin {} can not "
                "handle the full log"
            ).format(PLUGIN_NAME)
            # print(message)
            # noinspection PyCallByClass,PyTypeChecker
            QgsMessageLog.logMessage(message, PLUGIN_NAME, Qgis.Critical)


class QgsMessageBarFilter(logging.Filter):
    """
    A logging filter to decide whether the message should be passed and
    to QgsMessageBarHandler as enriched

    Description of keys:
        details: Longer body of the message. Can be set to empty string.
        duration: can be used to specify the message timeout in seconds. If ``duration``
            is set to 0, then the message must be manually dismissed by the user.
        success: boolean, defaults to False.
            Whether the message is success message or not
    """

    def filter(self, record: logging.LogRecord) -> bool:
        args = record.__dict__
        if "details" not in args:
            return False

        record.qgis_level = (  # type: ignore
            qgis_level(record.levelname)
            if not args.get("success", False)
            else Qgis.Success
        )
        record.duration = args.get("duration", self.bar_msg_duration(record.levelname))  # type: ignore # noqa E501
        return True

    @staticmethod
    def bar_msg_duration(logging_level: str) -> int:
        """Check default duration for messages in message bar based on level.

        :param logging_level: The Logging level
        :return: duration in seconds
        """
        if logging_level == "CRITICAL":
            return 12
        elif logging_level == "ERROR":
            return 10
        elif logging_level == "WARNING":
            return 6
        elif logging_level == "INFO":
            return 4
        elif logging_level == "DEBUG":
            return 4

        return 4


class QgsMessageBarHandler(logging.Handler):
    """A logging handler that will log messages to the QGIS message bar."""

    def __init__(self, msg_bar: Optional[QgsMessageBar] = None) -> None:
        self.msg_bar = msg_bar

        logging.Handler.__init__(self)

    def emit(self, record: logging.LogRecord) -> None:
        """
        Push info message to the QGIS message bar. Pass "extra" kwarg
        to logger to use with mandatory "details" key.

        :param record: logging record enriched with extra information from
            QgsMessageBarFilter
        """
        try:
            if self.msg_bar is not None:
                # noinspection PyArgumentList
                self.msg_bar.pushMessage(
                    title=record.message,
                    text=record.details,  # type: ignore
                    level=record.qgis_level,  # type: ignore
                    duration=record.duration,  # type: ignore
                )
        except MemoryError:
            pass  # This is handled in QgsLogHandler


def add_logging_handler_once(logger: logging.Logger, handler: logging.Handler) -> bool:
    """A helper to add a handler to a logger, ensuring there are no duplicates.

    :param logger: Logger that should have a handler added.
    :type logger: logging.logger

    :param handler: Handler instance to be added. It will not be added if an
        instance of that Handler subclass already exists.
    :type handler: logging.Handler

    :returns: True if the logging handler was added, otherwise False.
    :rtype: bool
    """
    class_name = handler.__class__.__name__
    for logger_handler in logger.handlers:
        if logger_handler.__class__.__name__ == class_name:
            return False

    logger.addHandler(handler)
    return True


def get_log_level_key(target: LogTarget) -> str:
    """Finds QSetting key for log level"""
    return setting_key("log_level", target.id)


def get_log_level_name(target: LogTarget) -> str:
    """Finds the log level name of the target"""
    return get_setting(get_log_level_key(target), target.default_level, str)


def get_log_level(target: LogTarget) -> int:
    """Finds log level of the target"""
    return logging.getLevelName(get_log_level_name(target))


def get_log_folder() -> Path:
    """
    Get Path to the log folder in QGIS profile directory.
    If it does not exist, create one.

    :return: Path to the log folder
    """
    old_log_dir = Path(plugin_path("logs"))
    if old_log_dir.exists():
        return old_log_dir
    log_dir = Path(profile_path("logs"))
    log_dir.mkdir(exist_ok=True)
    return log_dir


def setup_logger(  # noqa QGS105
    logger_name: str, iface: Optional[QgisInterface] = None
) -> logging.Logger:
    """Run once when the module is loaded and enable logging.


    :param logger_name: The logger name that we want to set up.
    :param iface: QGIS Interface

    Borrowed heavily from this:
    http://docs.python.org/howto/logging-cookbook.html

    Now to log a message do::
       LOGGER.debug('Some debug message')

    And to a message bar::
       LOGGER.info('Some bar message', extra={'details': 'details'})
       LOGGER.info('Some bar message', extra=bar_msg('details')) # With helper function
    """

    stream_level = get_log_level(LogTarget.STREAM)
    file_level = get_log_level(LogTarget.FILE)
    bar_level = get_log_level(LogTarget.BAR)

    logger = logging.getLogger(logger_name)
    logger.setLevel(min(stream_level, file_level))

    if logger_name != "test_plugin":
        file_formatter = logging.Formatter(
            "%(asctime)s - [%(levelname)-7s] - %(filename)s:%(lineno)d : %(message)s",
            "%d.%m.%Y %H:%M:%S",
        )
        file_handler = RotatingFileHandler(
            str(get_log_folder() / Path(f"{logger_name}.log")), maxBytes=1024 * 1024 * 2
        )
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(file_level)
        add_logging_handler_once(logger, file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(stream_level)
    console_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", "%d.%m.%Y %H:%M:%S"
    )
    console_handler.setFormatter(console_formatter)
    add_logging_handler_once(logger, console_handler)

    qgis_handler = QgsLogHandler()
    qgis_formatter = logging.Formatter("[%(levelname)-7s]- %(message)s")
    qgis_handler.setFormatter(qgis_formatter)
    add_logging_handler_once(logger, qgis_handler)

    if iface is None:
        try:
            from qgis.utils import iface  # type: ignore
        except ImportError:
            iface = None

    if iface is not None:
        qgis_msg_bar_handler = QgsMessageBarHandler(iface.messageBar())
        qgis_msg_bar_handler.addFilter(QgsMessageBarFilter())
        qgis_msg_bar_handler.setLevel(bar_level)
        add_logging_handler_once(logger, qgis_msg_bar_handler)

    return logger


def add_logger_msg_bar_to_widget(logger_name: str, widget: QWidget) -> None:
    """
    Adds QgsMessageBar to any widget if it is not already there.
    This message bar will be used in logging instead of iface message bar.
    :param logger_name: The logger name that we want modify
    :param widget: QWidget that will have the message bar
    """
    if not hasattr(widget, "message_bar"):
        layout: QLayout = widget.layout()
        widget.message_bar = QgsMessageBar(widget)  # type: ignore
        if isinstance(layout, QVBoxLayout):
            # noinspection PyArgumentList
            layout.insertWidget(0, widget.message_bar)
    use_custom_msg_bar_in_logger(logger_name, widget.message_bar)


def use_custom_msg_bar_in_logger(logger_name: str, msg_bar: QgsMessageBar) -> None:
    """
    Remove QgsMessageBarHandler that is using the iface message bar
    and use custom message bar instead

    :param logger_name: The logger name that we want modify
    :param msg_bar: message bar that is inside dialog, dockwidget or
        in some other widget
    """
    logger = logging.getLogger(logger_name)
    bar_level = get_log_level(LogTarget.BAR)

    for handler in logger.handlers[:]:
        if isinstance(handler, QgsMessageBarHandler):
            logger.removeHandler(handler)

    qgis_msg_bar_handler = QgsMessageBarHandler(msg_bar)
    qgis_msg_bar_handler.addFilter(QgsMessageBarFilter())
    qgis_msg_bar_handler.setLevel(bar_level)
    add_logging_handler_once(logger, qgis_msg_bar_handler)


def setup_task_logger(logger_name: str) -> logging.Logger:
    """Run once when the module is loaded and enable logging during tasks.

    :param logger_name: The logger name that we want to set up.
    """

    warnings.warn(
        "setup_task_logger() will be deprecated. Use setup_logger() instead.",
        PendingDeprecationWarning,
    )
    stream_level = get_log_level(LogTarget.STREAM)
    logger = logging.getLogger(f"{logger_name}_task")
    logger.setLevel(stream_level)
    logger.handlers = []

    qgis_handler = QgsLogHandler()
    qgis_formatter = logging.Formatter("[%(levelname)-7s]- %(message)s")
    qgis_handler.setFormatter(qgis_formatter)
    add_logging_handler_once(logger, qgis_handler)

    return logger


def teardown_logger(logger_name: str) -> None:
    """Remove all handlers from the logger

    :param logger_name: The logger name that we want to tear down.
    """
    logger = logging.getLogger(logger_name)
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
