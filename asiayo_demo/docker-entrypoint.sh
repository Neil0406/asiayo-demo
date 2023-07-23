#!/bin/sh
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
DJANGO_SUPERUSER_PASSWORD=$PASSWORD python manage.py createsuperuser --noinput --name $USER --email $USER
uwsgi --ini uwsgi.ini