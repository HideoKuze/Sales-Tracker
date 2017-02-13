from .forms import LoginForms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error
from django.contrib.auth import authenticate, login, logout
import MySQLdb
from django.template import loader
# Create your views here.

def profile(request):
	return render(request, 'tracker/profile.html', {})

def login(request):
	# this will be the first page someone who isn't signed in will see
	form = LoginForms()
	return render(request, 'tracker/login.html', {'form':form})

def sign_up(request):
	pass
