from django.shortcuts import render

from django.http.response import HttpResponse

from django.views.generic import View

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import authenticate, login
from django.contrib.sessions.models import Session

class user_login(View):
    
    form_class = AuthenticationForm
    template_name = 'login.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('OK')
            else:
                return HttpResponse('Account is inactive or has been deleted')
            
        return HttpResponse('Invalid form')
        return render(request, self.template_name, {'form': form})
    
class register(View):
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponse('You are already logged in! Please log out if you want to create a new account')
        
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('OK')
            else:
                return HttpResponse('Account is inactive or has been deleted')
            
        return HttpResponse('Invalid form')
        return render(request, self.template_name, {'form': form})
 
    