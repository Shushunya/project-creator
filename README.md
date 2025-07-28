# Project Scaffolder

Project Scaffolder is a Python-based CLI tool that quickly bootstraps new project directories using customizable YAML templates. Ideal for creating consistent project structures for scripts, CLI tools, libraries, and more.

---

## Features

- Generate project folders and files from simple YAML templates
- Support for nested directory structures
- Customizable default content in files (like `README.md`, `main.py`, etc.)
- Easy to extend with your own templates
- Minimal dependencies

---

## Installation

Clone the repo and install dependencies:

`git clone https://github.com/yourusername/project-scaffolder.git`
`cd project-scaffolder`
`pip install -r requirements.txt`


## Usage

Run the scaffolder using Python:

```bash
Copy
Edit
python -m scaffolder.main --name my_project --template templates/minimal.yaml
```
Arguments:

--name: Name of the project (used as the folder name)

--template: Path to the YAML file defining the structure

YAML Template Example
A basic minimal.yaml might look like this:

yaml
Copy
Edit
my_project:
  my_project:
    __init__.py: ""
    main.py: "# Main entry point"
  tests:
    __init__.py: ""
  README.md: "# My Project"
  requirements.txt: ""
  setup.py: ""
This generates:

markdown
Copy
Edit
my_project/
├── my_project/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── __init__.py
├── README.md
├── requirements.txt
└── setup.py
Project Structure
arduino
Copy
Edit
project_scaffolder/
├── scaffolder/
│   ├── main.py
│   ├── parser.py
│   ├── creator.py
│   └── utils.py
├── templates/
│   ├── minimal.yaml
│   └── cli_tool.yaml
├── tests/
├── README.md
├── requirements.txt
└── setup.py
Running Tests
bash
Copy
Edit
pytest tests/
Planned Features
 Template variable substitution (e.g., {{project_name}})

 Built-in templates for CLI tools, web apps, etc.

 Interactive CLI prompts

 Global CLI installation support

License
MIT License

