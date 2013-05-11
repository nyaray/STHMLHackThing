#!/bin/sh

ABSPATH=$(cd "$(dirname "$0")"; pwd)
cd $ABSPATH
export PYTHONPATH=.:$PYTHONPATH

python likealike/manage.py runserver
