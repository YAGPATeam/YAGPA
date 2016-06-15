from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
class player_manager(View):
    def get(self, request, *args, **kwargs):
        return render(self.request(), "tournament.thml" )