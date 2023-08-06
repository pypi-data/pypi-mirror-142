# python-plugin-framework
A plugin framework for applications written in Python.

Commands to build and push to PyPi:
```
rm -rf dist/*
python -m build
twine upload --config-file .pypirc dist/*
```