#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

python mange.py collectstatic --no-input
python manage.py migrate