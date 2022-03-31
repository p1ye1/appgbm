web:gunicorn gbm.wsgi:application --log-file - --log-level debug
python manage.py collectstatic--noinput
python manage.py migrate