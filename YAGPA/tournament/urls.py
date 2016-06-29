'''
Created on 15 juin 2016

@author: kicyfroth
'''

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<tournament_id>[0-9]{3})/player_manager/', views.player_manager.as_view(), name='player_manager'),    
]