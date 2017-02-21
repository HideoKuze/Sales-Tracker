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
# Create your views here.

def profile(request):
	return render(request, 'tracker/profile.html', {})

def login(request):
	# this will be the first page someone who isn't signed in will see
	form = LoginForms(request.POST)
	username = request.POST.get('username')
	password = request.POST.get('password')
	if username and password:
		#this line returns two values, a user object and a boolean flag 'created', 'true' if user is created and false if user already exists
		user,created = User.objects.get_or_create(username=username, password=password)
		if created:
			#if a new user is created save the user 
			user.set_password(password)
			user.save()
		#if the user alraedy exists
		user = authenticate(username=username, password=password)
		auth_login(request, user)
		return HttpResponse('success')
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