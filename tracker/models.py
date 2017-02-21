from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.

class LoginInfo(models.Model):
	username = models.CharField('', max_length=10)
	password = models.CharField('', max_length=15)