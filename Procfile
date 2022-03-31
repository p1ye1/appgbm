web: gunicorn gbm.wsgi:application --log-file - --log-level debug
python3 manage.py collectstatic--noinput
python3 manage.py migrate