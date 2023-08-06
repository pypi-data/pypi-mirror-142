#!/usr/bin/env bash

PY=/home/illiak/.cache/pypoetry/virtualenvs/marketa-iAkQGago-py3.9/bin/python
if ! test -f "$PY"; then
    SITEPACKAGES=$(python -c 'import site; print(site.getsitepackages()[0])')
    chmod +x $SITEPACKAGES/marketa/mk.sh
    ln -s $SITEPACKAGES/marketa/mk.sh /usr/local/bin/mk
fi