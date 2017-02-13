#custom backend
from django.conf import settings
from checkin.models import Question
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

class StaffBackend:
	def authenticate(self, username=None, password=None):
		try:
			user = Question.objects.get(username=username)
			if check_password(password, user.id_text):
				return user
			else:
				return None
		except Question.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			return Question.objects.get(pk=user_id)
		except Question.DoesNotExist:
			return None