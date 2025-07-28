from .parser import get_args
from .creator import create_project
from .config import CURRENT_DIR

def main():
    params = get_args()
    print(params)

    create_project(params["type"], params["name"], CURRENT_DIR)

if __name__ == "__main__":
    main()