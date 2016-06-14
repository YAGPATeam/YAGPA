'''
Created on 22 avr. 2016

@author: kicyfroth


from django import forms

class f_login(forms.Form):
    user_name = forms.CharField(label="user name", max_length=255)
    password = forms.PasswordInput("password")
''' 
    
    