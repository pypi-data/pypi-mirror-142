#!/bin/sh

sudo systemctl restart redis &
celery -A gview.worker.celery worker &
celery -A gview.p_worker.celery worker -B &
gunicorn -b 10.80.42.208:5000 gview.wsgi:app