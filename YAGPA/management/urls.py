'''
Created on 22 avr. 2016

@author: kicyfroth
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new/', views.new_tournament.as_view(), name='new'),
    url(r'^my_tournaments/', views.my_tournaments.as_view(), name='my_tournaments'),
    
]