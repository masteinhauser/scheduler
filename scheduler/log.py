# vim: tabstop=4 shiftwidth=4 softtabstop=4

import logging
import sys

NAME = 'scheduler'
logger = None


def get_logger():
    global logger

    if logger:
        return logger

    logger = logging.getLogger(NAME)
    log_handler = logging.StreamHandler(sys.stdout)
    fmt = logging.Formatter(fmt='%(asctime)s %(levelname)s: %(message)s',
                            datefmt='%F %H:%M:%S')
    log_handler.setFormatter(fmt)
    logger.addHandler(log_handler)
    logger.setLevel(logging.INFO)

    return logger


def set_level_debug():
    logger = get_logger()
    logger.setLevel(logging.DEBUG)
