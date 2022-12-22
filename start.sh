#!/bin/bash

python manage.py collectstatic

python manage.py migrate

gunicorn --reload --bind 0.0.0.0:8000 todolist.wsgi:application