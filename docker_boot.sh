#!/bin/sh
# boot file for starting the application in a docker container
source venv/bin/activate
flask db upgrade
exec gunicorn -b :5000 --access-logfile - --error-logfile - wsgi:app