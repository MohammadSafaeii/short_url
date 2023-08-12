import os
from celery import Celery
from django.conf import settings
# from analytics.tasks import run_asyncFillUrlUsageTable

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'short_url.settings')

app = Celery('short_url')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks()
