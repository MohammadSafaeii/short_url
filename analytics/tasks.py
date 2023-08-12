from celery import shared_task
from datetime import datetime, time, timedelta
from django.utils import timezone
from .views import cronFillUrlUsageTable


@shared_task
def run_asyncFillUrlUsageTable():
	cronFillUrlUsageTable()
