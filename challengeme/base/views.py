from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.http import HttpResponse
import datetime

from challengeme.base.models import Challenge, Instance, User, Charity

class LandingPage(TemplateView):
    template_name = "home.html"

def poop(request):
    now = datetime.datetime.now()
    html = "<html>sup bae it's %s</html>" % now
    return HttpResponse(html)

class UserDashboard(ListView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)

        # Get context objects.
        context['own_challenges'] = Instance.objects.filter(owner=self.request.user)
        context['challenges_in'] = self.request.user.participants.all()
        context['challenges_supporting'] = self.request.user.supporters.all()

        return context

    def get(self, request):
        if not request.user.is_authenticated():
            return render_to_response('base/templates/home.html')
        else:
            return TemplateResponse(request, template_name, context)
        
    
class AllChallengesView(ListView):
    model = Challenge


    def get_context_data(self, **kwargs):

        context = super(AllChallengesView, self).get_context_data(**kwargs)
        context['public_challenges'] = Instance.objects.all() 

        return context

    def get(self, request):
        if not request.user.is_authenticated():
            return render_to_response('base/templates/home.html')
        else:
            return TemplateResponse(request, template_name, context)

class AddChallenge(CreateView):
    # Creating new challenge, and instance of the challenge
    model = Challenge
    fields = ['title', 'description', 'owner', 'charity']
    fields.append(['note', 'goal_date', 'bounty', 'participants', 'supporters'])

