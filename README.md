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




