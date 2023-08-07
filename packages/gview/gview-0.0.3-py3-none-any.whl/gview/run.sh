#!/bin/sh

sudo systemctl restart redis &
celery -A worker.celery worker &
celery -A p_worker.celery worker -B &
gunicorn -b 10.80.42.208:5000 wsgi:app