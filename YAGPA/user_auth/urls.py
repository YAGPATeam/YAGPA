'''
Created on 10 juin 2016

@author: kicyfroth
'''
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^register/$', views.register, name='register'),
]