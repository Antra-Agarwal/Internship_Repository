"""
Application logger.
"""

import logging
import sys


def get_logger(
    name: str,
) -> logging.Logger:
    """
    Create and configure a logger.

    Args:
        name:
            Logger name.

    Returns:
        Configured logger.
    """

    logger = logging.getLogger(name)

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    logger.propagate = False

    return logger