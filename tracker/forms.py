#this will be where we create the model forms
from django import forms
from models import LoginInfo

class LoginForms(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
