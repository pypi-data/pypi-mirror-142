import logging

from logging.handlers import RotatingFileHandler

from .constants import BACKUP_COUNT, MAX_BYTES

formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")


def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    handler = RotatingFileHandler(log_file, maxBytes=MAX_BYTES,
        backupCount=BACKUP_COUNT)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
