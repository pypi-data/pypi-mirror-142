import logging
import os
from logging import Logger
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional, Union


def get_logger(
    name: Optional[str] = None,
    level: Optional[Union[str, int]] = None,
    file: Optional[Union[bool, str]] = None,
    show_file_path: Optional[bool] = None,
) -> Logger:
    """Configure a logger.

    Args:
        name (Optional[str], optional): Name for the logger. Included in log string prefix. Defaults to None.
        level (Optional[Union[str, int]], optional): Logging level -- CRITICAL: 50, ERROR: 40, WARNING: 30, INFO: 20, DEBUG: 10. Defaults to f"{name.upper()}_LOG_LEVEL" environment variable or INFO.
        file (Optional[Union[bool, str]], optional): File to write logs to. If True, logs will be written to a file in user's home directory. Defaults to f"{name.upper()}_FILE" environment variable or None.
        show_file_path (Optional[bool], optional): Show complete file path in log string prefix, rather than just filename. Defaults to level == DEBUG.

    Returns:
        Logger: The configured logger.
    """
    # create a new logger or return a reference to an already configured logger.
    logger = logging.getLogger(name)
    # if this is not the first call, the logger will already have handlers.
    if logger.handlers:
        return logger

    # check environment variables for kwargs that weren't provided.
    if file is None and name is not None:
        file = os.getenv(f"{name.upper()}_FILE")

    # set log level.
    level = (
        level
        if level is not None
        else os.getenv(
            f"{name.upper()}_LOG_LEVEL" if name else "LOG_LEVEL", logging.INFO
        )
    )
    if isinstance(level, str):
        level = logging.getLevelName(level.upper())
    logger.setLevel(level)

    # set formatting and handling.
    file_name_fmt = (
        "pathname"
        if show_file_path or show_file_path is None and level == logging.DEBUG
        else "filename"
    )
    formatter = logging.Formatter(
        f"[%(asctime)s][%(levelname)s]{'[%(name)s]' if name else ''}[%({file_name_fmt})s:%(lineno)d] %(message)s"
    )
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    # check if log file setup is needed.
    if file == True:
        file = Path.home() / f"{name}.log"
    if file:
        # create log directory if it doesn't currently exist.
        file.parent.mkdir(exist_ok=True, parents=True)
        # add file handler.
        file_handler = RotatingFileHandler(
            file, maxBytes=200_000_000, backupCount=1  # 20 MB
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # don't duplicate log messages.
    logger.propagate = False

    return logger
