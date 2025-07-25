import yaml
import os
from utils import templates_path, file_path
# to do list
# TODO: split into files
# TODO: add parsing args from console
# TODO: make a config file
# TODO: make config file for choosing project structure file
# TODO: add templates for files
# TODO: optimize yaml files

tmp = {
    "fastAPI": "fastAPI.yaml",
    "test": "test.yaml"
}

working_file_name = "../templates/main.yaml"

def write_project_name_to_yaml(project_type, name):

    # yaml_file = tmp[project_type]
    yaml_file = file_path(project_type + ".yaml")
    # open yaml file
    with open(yaml_file) as f:
        default_yaml = yaml.safe_load(f)

    # edit the project name
    for parameter in default_yaml:
        if parameter == "project_name":
            default_yaml[parameter] = name

    # write new yaml
    with open(working_file_name, "w") as f:
        yaml.dump(default_yaml, f)

    return working_file_name

current_dir = os.getcwd()

def create_structure(base_path, structure):
    for item in structure.items():
        name = item[0]
        content = item[1]
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w") as f:
                f.write(content or "")

def create_project(
        project_type,
        project_name,
        base_path=current_dir):
    file_name = write_project_name_to_yaml(project_type, project_name)
    with open(file_name) as f:
        yaml_file = yaml.safe_load(f)

    project_name = yaml_file["project_name"]
    structure = yaml_file["structure"]

    os.makedirs(project_name, exist_ok=True)
    create_structure(project_name, structure)


# create_project("fastAPI", "new try")