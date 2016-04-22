from django.shortcuts import render

from django.views.generic import View

from .forms import f_new
from django.http.response import HttpResponse

class new_tournament(View):
    
    form_class = f_new
    template_name = 'form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponse('OK')

        return render(request, self.template_name, {'form': form})
