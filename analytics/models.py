from django.db import models
from django.contrib.auth.models import User


class ShortUrlUsage(models.Model):
	shorturl = models.CharField(max_length=10)
	csrf_token = models.CharField(max_length=200)
	device = models.CharField(max_length=10)
	browser = models.CharField(max_length=20)
	date_create = models.DateTimeField('date used', auto_now_add=True)


class ShortUrlUsageLastDay(models.Model):
	shorturl = models.CharField(max_length=10)
	general_count = models.IntegerField()
	general_count_per_user = models.IntegerField()
	device_count = models.JSONField()
	device_count_per_user = models.JSONField()
	browser_count = models.JSONField()
	browser_count_per_user = models.JSONField()


class ShortUrlUsageLastWeek(models.Model):
	shorturl = models.CharField(max_length=10)
	general_count = models.IntegerField()
	general_count_per_user = models.IntegerField()
	device_count = models.JSONField()
	device_count_per_user = models.JSONField()
	browser_count = models.JSONField()
	browser_count_per_user = models.JSONField()


class ShortUrlUsageLastMonth(models.Model):
	shorturl = models.CharField(max_length=10)
	general_count = models.IntegerField()
	general_count_per_user = models.IntegerField()
	device_count = models.JSONField()
	device_count_per_user = models.JSONField()
	browser_count = models.JSONField()
	browser_count_per_user = models.JSONField()
