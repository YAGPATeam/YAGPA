from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class player_manager(TemplateView):
    
    template_name = "tournament/tournament.html"
    
    def get_context_data(self, **kwargs):
        context = super(player_manager, self).get_context_data(**kwargs)
        context['tournament_id'] = self.kwargs['tournament_id']
        return context