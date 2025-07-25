import argparse, pathlib
from config import DEFAULT_PROJECT_TYPE, DEFAULT_PROJECT_NAME, CURRENT_DIR
from utils import get_available_types

# TODO: add usage msg
# TODO: add description

project_types = get_available_types()

def get_args() -> dict:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-n", "--name",
        default=DEFAULT_PROJECT_NAME,
        type=str)
    parser.add_argument(
        "-t", "--type",
        choices=project_types,
        default=DEFAULT_PROJECT_TYPE,
        help="Type of project to create (default: %(default)s)"
    )
    parser.add_argument(
        "path",
        type=pathlib.Path,
        default=CURRENT_DIR
    )
    data = parser.parse_args()
    return vars(data)
