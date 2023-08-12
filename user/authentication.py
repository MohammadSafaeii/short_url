from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class EmailBackend(ModelBackend):
	def authenticate(self, request, username=None, email=None, password=None, **kwargs):
		user_model = get_user_model()
		if username:
			try:
				user = user_model.objects.get(username=username)
			except user_model.DoesNotExist:
				return None
			else:
				if user.check_password(password):
					return user
			return None
		else:
			try:
				user = user_model.objects.get(email=email)
			except user_model.DoesNotExist:
				return None
			else:
				if user.check_password(password):
					return user
			return None

	def get_user(self, user_id):
		user_model = get_user_model()
		try:
			return user_model.objects.get(pk=user_id)
		except user_model.DoesNotExist:
			return None
