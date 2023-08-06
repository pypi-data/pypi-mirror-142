import logging
import sys
from typing import Any, Dict, Optional

from .custom_logging import bar_msg
from .resources import plugin_name

LOGGER = logging.getLogger(plugin_name())


class MsgBar:
    """
    This static class is used to log messages to the Qgis message bar.
    Uses custom_logging.py's QgsMessageBarHandler under the hood.

    bar_msg could be used like this:
    MsgBar.exception("main message", **bar_msg)
    """

    KWARGS: Dict[str, Any] = (
        {}
        if sys.version_info.major == 3 and sys.version_info.minor < 8
        else {"stacklevel": 2}
    )

    @staticmethod
    def info(
        message: Any,
        details: Any = "",
        duration: Optional[int] = None,
        success: bool = False,
    ) -> None:
        """
        Logs info messages to message bar and to other logging handlers
        :param message: Header of the message
        :param details: Longer body of the message. Can be set to empty string.
        :param duration: can be used to specify the message timeout in seconds. If
            ``duration`` is set to 0, then the message must be manually dismissed
            by the user.
        :param success: Whether the message is success message or not
        """

        LOGGER.info(
            str(message), extra=bar_msg(details, duration, success), **MsgBar.KWARGS
        )
        if details != "":
            LOGGER.info(str(details), **MsgBar.KWARGS)

    @staticmethod
    def warning(
        message: Any,
        details: Any = "",
        duration: Optional[int] = None,
        success: bool = False,
    ) -> None:
        """
        Logs warning messages to message bar and to other logging handlers
        :param message: Header of the message
        :param details: Longer body of the message. Can be set to empty string.
        :param duration: can be used to specify the message timeout in seconds. If
            ``duration`` is set to 0, then the message must be manually dismissed
            by the user.
        :param success: Whether the message is success message or not
        """
        LOGGER.warning(
            str(message), extra=bar_msg(details, duration, success), **MsgBar.KWARGS
        )
        if details != "":
            LOGGER.warning(str(details), **MsgBar.KWARGS)

    @staticmethod
    def error(
        message: Any,
        details: Any = "",
        duration: Optional[int] = None,
        success: bool = False,
    ) -> None:
        """
        Logs error without traceback of risen exception to message bar and to
        other logging handlers
        :param message: Header of the message
        :param details: Longer body of the message. Can be set to empty string.
        :param duration: can be used to specify the message timeout in seconds. If
            ``duration`` is set to 0, then the message must be manually dismissed
            by the user.
        :param success: Whether the message is success message or not
        """
        LOGGER.error(
            str(message), extra=bar_msg(details, duration, success), **MsgBar.KWARGS
        )
        if details != "":
            LOGGER.error(str(details), **MsgBar.KWARGS)

    @staticmethod
    def exception(
        message: Any,
        details: Any = "",
        duration: Optional[int] = None,
        success: bool = False,
    ) -> None:
        """
        Logs error with traceback of risen exception to message bar and to
        other logging handlers
        :param message: Header of the message
        :param details: Longer body of the message. Can be set to empty string.
        :param duration: can be used to specify the message timeout in seconds. If
            ``duration`` is set to 0, then the message must be manually dismissed
            by the user.
        :param success: Whether the message is success message or not
        """
        LOGGER.exception(
            str(message), extra=bar_msg(details, duration, success), **MsgBar.KWARGS
        )
        if details != "":
            LOGGER.error(str(details), **MsgBar.KWARGS)
