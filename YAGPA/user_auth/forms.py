'''
Created on 22 avr. 2016

@author: kicyfroth
'''

from django import forms
from django.utils import six
from djng.forms import NgDeclarativeFieldsMetaclass, NgFormValidationMixin

class f_login(six.with_metaclass(NgDeclarativeFieldsMetaclass, NgFormValidationMixin, forms.Form)):
    user_name = forms.CharField(label="user name", max_length=255)
    password = forms.PasswordInput("password")

    
    