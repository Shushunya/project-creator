from config import BASE_PATH, TEMPLATES_PATH, PROJECT_TEMPLATES_PATH

from pathlib import Path

templates_path = Path(BASE_PATH) / TEMPLATES_PATH / PROJECT_TEMPLATES_PATH

def get_available_types():

    b = [item.stem for item in templates_path.iterdir() if item.suffix == ".yaml"]
    return tuple(b)

def file_path(file_name: str):
    return templates_path / file_name
