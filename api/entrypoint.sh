#!/bin/bash

set -e  # exit on error

echo "Running collectstatic..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate --noinput

#creating superuser
echo "Checking if superuser exists..."
if python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
import sys
sys.exit(0) if User.objects.filter(is_superuser=True).exists() else sys.exit(1)
"; then
    echo "Superuser already exists. Skipping creation."
else
    echo "Creating superuser..."
    python manage.py createsuperuser \
        --noinput \
        --username "$DJANGO_SUPERUSER_USERNAME" \
        --email "$DJANGO_SUPERUSER_EMAIL"

    python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
user = User.objects.get(username='$DJANGO_SUPERUSER_USERNAME');
user.set_password('$DJANGO_SUPERUSER_PASSWORD');
user.save()
"
fi

#starting gunicorn server
echo "Starting Gunicorn..."
exec gunicorn --bind 0.0.0.0:8000 --workers 3 api.wsgi:application
exec "$@"

# #!/bin/bash

# set -e  # exit on error
# echo "Running collectstatic..."
# python manage.py collectstatic --noinput

# echo "Running migrations..."
# python manage.py migrate --noinput

# echo "Creating superuser..."
# python manage.py createsuperuser --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL
#     --noinput || true

# echo "Starting Gunicorn..."
# exec gunicorn --bind 0.0.0.0:8000 --workers 3 api.wsgi:application

# exec "$@"