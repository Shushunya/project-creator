import os
from dotenv import load_dotenv


load_dotenv()

CURRENT_DIR = os.getcwd()

DEFAULT_PROJECT_TYPE = os.getenv("DEFAULT_PROJECT_TYPE=", "CLI")
DEFAULT_PROJECT_NAME = os.getenv("DEFAULT_PROJECT_NAME", "Local new name")

BASE_PATH = os.getenv("BASE_PATH", "D:\projects\project starter")
TEMPLATES_PATH = os.getenv("TEMPLATES_PATH", "/templates")
PROJECT_TEMPLATES_PATH = os.getenv("PROJECT_TEMPLATES_PATH", "/projects")

USAGE_MSG = os.getenv("USAGE_MSG", "")
EPILOG_MSG = os.getenv("EPILOG_MSG", "")
DESCRIPTION_MSG = os.getenv("DESCRIPTION_MSG", "")

HELP_PATH = os.getenv("HELP_PATH", "")
HELP_NAME = os.getenv("HELP_NAME", "")
HELP_TYPE = os.getenv("HELP_TYPE", "")
HELP_VERSION = os.getenv("HELP_VERSION", "")