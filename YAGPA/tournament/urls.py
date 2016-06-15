'''
Created on 15 juin 2016

@author: kicyfroth
'''
'''
Created on 10 juin 2016

@author: kicyfroth
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tournament/[0-9]{1,10}/player_manager/', views.player_manager.as_view(), name='player manager'),    
]