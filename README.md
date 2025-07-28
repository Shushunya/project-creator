# Project Scaffolder CLI

A Python command-line tool to quickly scaffold project directories and files based on predefined YAML templates. Ideal for creating consistent project structures for scripts, CLI tools, libraries, and more.

## Features

- Create empty project structures from templates  
- Support for nested directory structures
- Supports multiple project types (CLI, FastAPI, etc.)  
- Uses YAML files to define project layouts  
- CLI interface with `argparse`  
- Customizable default content in files (like README.md, main.py, etc)
- Editable and extensible templates  

## Getting Started

1. Clone the repository:

    `git clone https://github.com/Shushunya/project-creator.git`

    `cd project-creator`

2. Create a virtual environment 

    `python -m venv .venv`

3. Activate the virtual environment

    `.venv\Scripts\activate` (on Windows)

    `source .venv/bin/activate`

4. Install the package in editable mode

    `pip install -e .`

5. Verify installation

    `scaffold --help`

## Usage

1. Install the package in editable mode:

   `pip install -e .`

2. Run the CLI:

   `scaffold <path> [--name project_name] [--type project_type]`

   Example:

   `scaffold . --name testy --type CLI`
   or `scaffold . -n testy -t CLI`

   It will generate a new directory `testy` with the following structure:
    ```
    testy
    ├── app/
    │   ├── main.py                  
    │   ├── module1.py       
    │   ├── config.py        
    │   ├── utils.py
    │   └── __init__.py
    ├── templates/
    ├── tests/
    │   └── __init__.py
    ├── .env
    ├── .gitignore
    ├── pyproject.toml
    ├── requirements.txt
    └── README.md
    ```


## Project Structure

```
.
├── app/
│   ├── main.py          # Entry point
│   ├── parser.py        # Argument parsing logic
│   ├── creator.py       # Project generation logic
│   ├── config.py        # Config and paths
│   ├── utils.py
│   └── __init__.py
├── templates/
│   └── projects/
│       ├── CLI.yaml
│       ├── CLI_DB.yaml
│       ├── fastAPI.yaml
│       └── tmp.yaml
├── tests/
│   └── __init__.py
├── .env
├── .env.sample
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── setup.py
└── README.md
```