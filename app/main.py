from parser import get_args
from creator import create_project
from config import CURRENT_DIR

params = get_args()
print(params)

create_project(params["type"], params["name"], CURRENT_DIR)
