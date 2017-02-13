#this will be where we create the model forms
from django import forms
from models import LoginInfo

class LoginForms(forms.ModelForm):

	class Meta:
		model = LoginInfo
		fields = ('username', 'password')