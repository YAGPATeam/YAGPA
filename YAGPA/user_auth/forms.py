'''
Created on 22 avr. 2016

@author: kicyfroth
'''

from django import forms
from django.utils import six
from djng.forms import NgDeclarativeFieldsMetaclass, NgFormValidationMixin, NgModelFormMixin, NgForm

class f_login(six.with_metaclass(NgDeclarativeFieldsMetaclass, NgFormValidationMixin, forms.Form)):
    user_name = forms.CharField(label="user name", max_length=255)
    password = forms.PasswordInput("password")

    
class f_register(NgModelFormMixin, NgForm):
    user_name = forms.CharField(label="user name", max_length=255)
    user_email = forms.EmailField(label="email")
    password = forms.PasswordInput("password")