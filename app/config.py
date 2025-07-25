import os
from dotenv import load_dotenv

load_dotenv()

CURRENT_DIR = os.getcwd()

DEFAULT_PROJECT_TYPE = os.getenv("DEFAULT_PROJECT_TYPE=", "CLI")
DEFAULT_PROJECT_NAME = os.getenv("DEFAULT_PROJECT_NAME", "Local new name")

BASE_PATH = os.getenv("BASE_PATH", "D:\projects\project starter")
TEMPLATES_PATH = os.getenv("TEMPLATES_PATH", "/templates")
PROJECT_TEMPLATES_PATH = os.getenv("PROJECT_TEMPLATES_PATH", "/projects")
