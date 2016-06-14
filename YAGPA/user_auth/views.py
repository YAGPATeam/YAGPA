from django.shortcuts import render

from django.http.response import HttpResponse

from django.views.generic import View

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate, login
from django.contrib.sessions.models import Session

class user_login(View):
    
    form_class = AuthenticationForm
    template_name = 'form_login.html'
    
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
                return HttpResponse('Invalid user')
            
        return HttpResponse('Invalid form')
        return render(request, self.template_name, {'form': form})
    
'''def user_register(request):
    
    if request.user.is_authenticated():
    # Do something for authenticated users.
        
    else:
    # Do something for anonymous users.
 '''   
    