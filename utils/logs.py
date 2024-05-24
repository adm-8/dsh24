"""Provides functions to create loggers."""

import logging
from typing import Text
import sys

_log_format = f"%(asctime)s - [%(levelname)s] - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"


def get_file_handler(file_path) -> logging.FileHandler:
    """Get file handler.
    Returns:
        logging.FileHandler which logs into file "process_log.log"
    """
    handler = logging.FileHandler(file_path)
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(_log_format))
    return handler


def get_stream_handler() -> logging.StreamHandler:
    """Get console handler.
    Returns:
        logging.StreamHandler which logs into stdout
    """
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(_log_format))
    return handler


def get_logger(file_path: str, name: Text = __name__) -> logging.Logger:
    """Get logger.
    Args:
        name {Text}: logger name
    Returns:
        logging.Logger instance
    """

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate outputs in Jypyter Notebook
    if logger.hasHandlers():
        logger.handlers.clear()

    if file_path:
        logger.addHandler(get_file_handler(file_path))
    else:
        logger.addHandler(get_stream_handler())

    return logger
