#!/bin/bash
# ============================================================
# Django Application Startup Script
# Project: django-azure-events-databricks-ref-impl
# Author: Aruna Kishore
# ============================================================


# -----------------------------
# Step 3: Run database migrations
# -----------------------------
echo "Running Django database migrations..."
python manage.py makemigrations core_users
python manage.py migrate

# -----------------------------
# Step 4: Collect static files (optional for production)
# -----------------------------
if [ "$1" == "--collectstatic" ]; then
    echo "Collecting static files..."
    python manage.py collectstatic --noinput
fi

# -----------------------------
# Step 5: Run Django server
# -----------------------------
echo "Starting Django development server..."
python manage.py runserver 0.0.0.0:8000

# -----------------------------
# Step 6: Done
# -----------------------------
echo "Django application is up and running!"
