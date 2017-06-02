from .forms import LoginForms, QuantityForms
from .models import Product, ExtendedProfile, RevenueInfo, Purchases
from django.shortcuts import render, redirect
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
import csv
from django.utils.six.moves import range
from django.http import StreamingHttpResponse
from django.db.models import Sum
# Create your views here.

class Echo(object):
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value

def export_info(request):
    """A view that streams a large CSV file."""
    # Generate a sequence of rows. The range is based on the maximum number of
    # rows that can be handled by a single sheet in most spreadsheet
    # applications.
    rows = (["Row {}".format(idx), str(idx)] for idx in range(65536))
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse((writer.writerow(row) for row in rows),
                                     content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    return response


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
				#redirect them to their profile page
				return redirect(profile)
			else:
				return HttpResponse('invalid username/password combo')
		else:
			#redirect user to new page to create them a new account
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

def product_page(request):
	all_products = Product.objects.all()
	quantity_forms = QuantityForms(request.POST)
	quantity = request.POST.get('amount')
	grand_total = RevenueInfo.user_total
	current_user = request.user
	#buyer = User.
	if quantity > 0:
		#ExtendedProfile().amount_spent += (quantity * Product.price_CAD)
		#RevenueInfo().user_total += int(quantity)
		return HttpResponse(current_user.product_set.all()[0].description)
	return render(request,'tracker/product_page.html', {'all_products':all_products, 'quantity_forms':quantity_forms})

def product_details(request, object_id):
	product = Product.objects.get(id=object_id)
	return render(request, 'tracker/product_details.html', {'product':product})
