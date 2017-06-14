from django.conf.urls import url
from . import views

urlpatterns = [url(r'^profile', views.profile, name='profile'),
url(r'^login', views.login, name='login'),
url(r'^export_info', views.export_info, name='export_info'),
url(r'^product_page', views.product_page, name='product_page'),
url(r'^(?P<object_id>[0-9]+)/$', views.product_details, name='product_details'),
url(r'^upload_pic', views.upload_pic, name='upload_pic'),
url(r'^album', views.album, name='album'),
]
