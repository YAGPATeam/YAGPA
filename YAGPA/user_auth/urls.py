'''
Created on 10 juin 2016

@author: kicyfroth
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/', views.user_login.as_view(), name='login'),    
]