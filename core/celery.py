import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# celery.py

# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
# from django.conf import settings

# # Set the default Django settings module for Celery
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")

# app = Celery("project_name")

# # Load task settings from Django's settings.py
# app.config_from_object("django.conf:settings", namespace="CELERY")

# # Automatically discover tasks in all installed apps
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)