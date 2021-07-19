#!/bin/bash
source /home/debian/code/syrovezhko/env/bin/activate
exec gunicorn -c "/home/debian/code/syrovezhko/djangowebsite/gunicorn_config.py" config.wsgi
