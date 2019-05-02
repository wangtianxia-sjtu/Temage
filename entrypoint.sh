supervisord -n &
pwd
uwsgi --socket :8001 --module Django.wsgi &