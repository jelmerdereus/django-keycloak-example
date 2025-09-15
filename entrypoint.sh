#!/usr/bin/env bash
set -euo pipefail

# Optional: wait a bit for a DB if needed (uncomment or customize)
# sleep 3

# Apply database migrations
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Create superuser if all required env vars are present
# Django reads password from DJANGO_SUPERUSER_PASSWORD when --noinput is used
if [[ -n "${DJANGO_SUPERUSER_USERNAME:-}" && -n "${DJANGO_SUPERUSER_EMAIL:-}" && -n "${DJANGO_SUPERUSER_PASSWORD:-}" ]]; then
  python manage.py createsuperuser \
    --noinput \
    --username "${DJANGO_SUPERUSER_USERNAME}" \
    --email "${DJANGO_SUPERUSER_EMAIL}" \
  || true
fi

# Start Django development server (replace with gunicorn if desired)
python manage.py runserver 0.0.0.0:8000