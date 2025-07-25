import argparse, pathlib

from config import (DEFAULT_PROJECT_TYPE, DEFAULT_PROJECT_NAME,
                    USAGE_MSG, DESCRIPTION_MSG, EPILOG_MSG,
                    HELP_PATH, HELP_NAME, HELP_TYPE, HELP_VERSION)
from utils import get_available_types


# TODO: make toml and get version from there
VERSION = "0.1.0"
project_types = get_available_types()

def get_args() -> dict:
    parser = argparse.ArgumentParser(
        usage=USAGE_MSG,
        description=DESCRIPTION_MSG,
        epilog = EPILOG_MSG
    )

    parser.add_argument(
        "path",
        type=pathlib.Path,
        help=HELP_PATH,

    )
    parser.add_argument(
        "-n", "--name",
        default=DEFAULT_PROJECT_NAME,
        type=str,
        help=HELP_NAME
    )
    parser.add_argument(
        "-t", "--type",
        choices=project_types,
        default=DEFAULT_PROJECT_TYPE,
        help=HELP_TYPE
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f'%(prog)s {VERSION}',
        help=HELP_VERSION
    )

    data = parser.parse_args()
    return vars(data)
