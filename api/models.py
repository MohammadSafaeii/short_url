from django.db import models
from django.contrib.auth.models import User


class urlHashmap(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
	longurl = models.CharField(max_length=255)
	shorturl = models.CharField(max_length=10, unique=True)

	def __str__(self):
		return self.shorturl
