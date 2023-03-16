#!/bin/sh
set -e
python manage.py create_db
flask db upgrade
python manage.py run -h 0.0.0.0 -p 5000