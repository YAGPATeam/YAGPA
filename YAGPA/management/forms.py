'''
Created on 22 avr. 2016

@author: kicyfroth
'''

from django import forms
from django.utils import six
from djng.forms import NgDeclarativeFieldsMetaclass, NgFormValidationMixin

class f_new(six.with_metaclass(NgDeclarativeFieldsMetaclass, NgFormValidationMixin, forms.Form)):
    name = forms.CharField(label="name", max_length=255)
    shortname = forms.CharField(label="short name", max_length=50)
    location = forms.CharField(label="location", max_length=255)
    director = forms.CharField(label="director", max_length=255)
    begin_date = forms.DateField(label="begin date")
    end_date = forms.DateField(label="end date")
    CHOICES=[('macmahon','Mac Mahon'),
         ('swiss','Swiss'),
         ('swiss_cat','Swiss with categories')]
    system = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), label='system')
    nb_rounds = forms.DecimalField(label="Numbre of rounds", max_digits=3)
    
    
    