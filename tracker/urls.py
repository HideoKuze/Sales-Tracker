from django.conf.urls import url
from . import views

urlpatterns = [url(r'^profile', views.profile, name='profile'),
url(r'^login', views.login, name='login')
]
