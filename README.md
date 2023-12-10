# django_model

# Stop the Django development server if it's running

# Check for other processes using the database file

# Verify your database connection settings in settings.py

# Remove the database file (Make sure you have a backup if needed)

- rm db.sqlite3

# Recreate the database and apply migrations

- python manage.py makemigrations
- python manage.py migrate

# Create a superuser

- python manage.py createsuperuser
