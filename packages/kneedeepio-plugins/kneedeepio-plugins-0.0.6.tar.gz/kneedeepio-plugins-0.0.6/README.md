# python-plugin-framework
A plugin framework for applications written in Python.

FIXME: Write a readme about the library, not how to build it.

Commands to build and push to PyPi:
 * Install build dependencies:
```
pip install --upgrade -r requirements.txt
```

 * Run tests and such:
```
python ./analysis_pylint.py
python ./analysis_coverage.py
python ./analysis_radon.py
```

 * Build and upload:
```
rm -rf dist/*
python -m build
twine upload --config-file .pypirc dist/*
```
