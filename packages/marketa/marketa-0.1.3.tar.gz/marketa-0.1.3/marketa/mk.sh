#!/usr/bin/env bash

# if development environment - activate venv and launch cli frontend
PY=/home/illiak/.cache/pypoetry/virtualenvs/marketa-iAkQGago-py3.9/bin/python
if test -f "$PY"; then
    $PY /home/illiak/projects/marketa/marketa/cli.py $@
else
    SITEPACKAGES=$(python -c 'import site; print(site.getsitepackages()[0])')
    python3 $SITEPACKAGES/marketa/cli.py $@
fi
