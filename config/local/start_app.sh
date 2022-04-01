#!/bin/bash
set -x

python check_db.py
./manage.py migrate
./manage.py runserver 0.0.0.0:8888