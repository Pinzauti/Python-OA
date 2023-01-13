# CERN OA

## How to run

First of all you have to create your virtual environment (`python3 -m venv env`). Then activate it and then execute the following commands:
```bash
pip install .                           # It installs the package
python3 -m cern_oa.dep_graph            # It executes the script
```

## How to test

```bash
pip install .[test]                     # It installs the package and the test dependencies
python3 -m pytest                       # It executes the tests
```

## File structure
The project has the following file structure.

    .
    ├── .github/                                # Github actions
    │   └── workflows/                          # Workflows                         
    │       ├── pylint.yml                      # Pylint workflow
    │       └── python-app.yml                  # Python workflow
    ├── src/                                    # Source code
    │   └── cern_oa/                            # Package
    │       ├── tests/                          # Tests
    │       │   ├── __init__.py                 # Init file
    │       │   └── test_dep_graph.py           # Tests for dep_graph.py
    │       ├── tmp/                            # Temporary files
    │       │   └── deps.json                   # Example json
    │       ├── __init__.py                     # Package init
    │       └── dep_graph.py                    # Main script
    ├── .gitignore                              # Git ignore file
    ├── LICENSE                                 # License file
    ├── pyproject.toml                          # Package configuration file
    ├── .pylintrc                               # Pylint configuration file
    └── README.md                               # This file




