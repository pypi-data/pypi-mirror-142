# ha-sts-plugin-library
This is the library that should be imported when writing a plugin for the ha-sts server.

Commands to build and push to PyPi:
```
rm -rf dist/*
python -m build
twine upload --config-file .pypirc dist/*
```
