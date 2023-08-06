__version_info__ = (0, 9, 0)
__version__ = '.'.join(map(str, __version_info__))

__all__ = ['read_level_from_args', 'get_default_logger']

import argparse as _argparse
import logging as _logging
import os as _os
from typing import Optional as _Optional


def read_level_from_args() -> int:
    """
    Called when a module wants to get log level using arguments.
    """
    parser = _argparse.ArgumentParser()
    parser.add_argument('-l', '--log', default='INFO', type=str)
    args, _ = parser.parse_known_args()
    log_level = args.log
    numeric_level = getattr(_logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {log_level}')
    return numeric_level


if _os.environ.get('READ_LOG_ARGS', False):
    default_log_level = read_level_from_args()
else:
    default_log_level = _logging.WARNING
print(f'Default log level set to: {_logging.getLevelName(default_log_level)}')


def get_default_logger(name: str, format_: str = '[%(asctime)s] [%(name)s]: '
                                                 '[%(levelname)s] %(message)s',
                       filepath: _Optional[str] = './output.log',
                       date_format: str = '%m-%d-%Y %H:%M:%S',
                       truncate_name: bool = True) -> _logging.Logger:
    """
    Using the provided arguments, gets an instance of a logger of the given
    name and sets it up.

    PARAMETERS
    ----------
    name
        The name of the module or component this logger is for.
    format_
        The format the messages should follow. See `format_`.
    filepath
        The path to the file to write the logs to. Set to None to not have a
        log file.
    date_format
        The format for the date in the logs.
    truncate_name
        Whether to truncate the name to the last phrase after the last '.'
        character.

    RETURNS
    -------
    -
        Returns the logger.
    """
    formatter = _logging.Formatter(format_, datefmt=date_format)

    logger = _logging.getLogger(name.split('.')[-1] if truncate_name else name)
    logger.setLevel(default_log_level)

    ch = _logging.StreamHandler()
    ch.setLevel(default_log_level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    if filepath is not None:
        fh = _logging.FileHandler(filepath)
        fh.setLevel(_logging.INFO)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
