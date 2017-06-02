from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django import forms, views
from django.db.models import Sum
from django.core.urlresolvers import reverse

# Create your models here.
#LoginInfo is not being used, LoginForms in forms.py is
class LoginInfo(models.Model):
	username = models.CharField('', max_length=10)
	password = models.CharField('', max_length=15)

class ExtendedProfile(models.Model):
	user = models.OneToOneField(User)
	amount_spent = models.DecimalField(max_digits=6, decimal_places=2, default=0)

	#@classmethod tells the class to act on itself instead of an instance of itself
	@classmethod
	def total_amount(cls):
		#returns a dictionary
		return cls.objects.all().aggregate(total=Sum('amount_spent'))

class RevenueInfo(models.Model):
	#here we access the dictionary
	user_total = ExtendedProfile().total_amount()['total']
	total_amount_spent = models.DecimalField("Total User Revenue", max_digits=6, decimal_places=2, default=user_total)

#pretty sure this is useless because the User model can be used as the buyer
class Buyer(models.Model):
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    
    def __str__(self):
    	return self.user_name

class Product(models.Model):
	purchase = models.ManyToManyField(settings.AUTH_USER_MODEL, through="Purchases")
	category = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	description = models.TextField()
	#photo = models.ImageField()
	price_CAD = models.DecimalField(max_digits=6, decimal_places=2)
	quantity = models.DecimalField(max_digits=2, decimal_places=0, null=True, editable=True)

	def get_absolute_url(self):
		return reverse("product_details", args=[self.id]) 


class Purchases(models.Model):
	buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	date_bought = models.DateField(null=True)



