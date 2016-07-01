from django.shortcuts import render

from django.http.response import HttpResponse

from django.views.generic import View

import xml.etree.cElementTree as ET

from .forms import f_new

from django.contrib.auth.decorators import login_required


class new_tournament(View):
    
    form_class = f_new
    template_name = 'form_new_tournament.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            
            
            
            return HttpResponse('OK')

        return render(request, self.template_name, {'form': form})


class my_tournaments(View):
    
    template_name = "base.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'data': "List of tournaments"})
