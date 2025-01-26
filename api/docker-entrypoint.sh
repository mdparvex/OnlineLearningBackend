#!/bin/bash

echo "Flush the manage.py command it any"

#while ! python manage.py flush --no-input 2>&1; do
  #echo "Flusing django manage command"
  #sleep 3
#done

echo "Migrate the Database at startup of project"

# Wait for few minute and run db migraiton
#while ! python manage.py makemigrations  2>&1; do
   #echo "Migration is in progress status"
   #sleep 3
#done

while ! python manage.py migrate --fake  2>&1; do
   echo "Migration is in progress status"
   sleep 3
done

python manage.py collectstatic --noinput \
   && gunicorn api.wsgi:application --bind 0.0.0.0:8000
#python manage.py collectstatic --noinput \
#   &&  python manage.py runserver 0.0.0.0:8000


echo "Django docker is fully configured successfully."

exec "$@"
