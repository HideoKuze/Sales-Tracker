#this will be where we create the model forms
from django import forms
from models import LoginInfo
from tracker.models import ExtendedProfile

class LoginForms(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

class QuantityForms(forms.Form):
	amount = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': "Enter Quantity"}))

class ImageUploadForm(forms.ModelForm):
	#model to store the information about the pictures
	class Meta:
		model = ExtendedProfile
		fields = ['img']