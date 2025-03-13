#!/usr/bin/env bash

python manage.py collectstatic --noinput
#python manage.py migrate --noinput
echo "Flush the manage.py command it any"

while ! python manage.py flush --no-input 2>&1; do
  echo "Flusing django manage command"
  sleep 3
done

echo "Migrate the Database at startup of project"

# Wait for few minute and run db migraiton
while ! python manage.py migrate  2>&1; do
   echo "Migration is in progress status"
   sleep 3
done
#run server
#python -m gunicorn --bind 0.0.0.0:8000 api.wsgi:application
gunicorn --bind 0.0.0.0:8000 api.wsgi:application

echo "Django docker is fully configured successfully."

exec "$@"