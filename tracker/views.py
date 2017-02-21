from .forms import LoginForms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
import MySQLdb
from django.template import loader
from django.db import IntegrityError
# Create your views here.

def profile(request):
	return render(request, 'tracker/profile.html', {})

def login(request):
	# this will be the first page someone who isn't signed in will see
	form = LoginForms(request.POST)
	username = request.POST.get('username')
	password = request.POST.get('password')
	if username and password:
		exists = User.objects.filter(username=username).exists()
		if exists:
			user = authenticate(username=username, password=password)
			if user is not None:
				auth_login(request, user)
				return HttpResponse('Logged in')
			else:
				return HttpResponse('invalid username/password combo')
		else:
			User.objects.create_user(username=username, password=password)
			user = authenticate(username=username, password=password)
			auth_login(request, user)
			return HttpResponse('created new user')	
	else:
		return render(request, 'tracker/login.html', {'form': form})

def sign_up(request):
	pass


"""if user is not None:
		login(request, user)
		# Redirect to a success page.
		return HttpResponse('good')
	else:
		return HttpResponse('bad')

	return render(request, 'tracker/login.html', {'form': form})"""

"""try:
            #this line returns two values, a user object and a boolean flag 'created', 'true' if user is created and false if user already exists
			user,created = User.objects.get_or_create(username=username, password=password)
			#if user is new
			if created:
				user.set_password(password)
				user.save()
			user = authenticate(username=username, password=password)
			auth_login(request, user)
			return HttpResponse('success')
		except IntegrityError:
			user = authenticate(username=username, password=password)
			auth_login(request, user)
			return HttpResponse('good') """