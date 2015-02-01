from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.http import HttpResponse
import datetime
from django.template.response import TemplateResponse

from challengeme.base.models import Challenge, Instance, User, Charity
from django.contrib.auth.decorators import login_required

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
        context['challenges_in'] = self.request.user.participants.all
        context['challenges_supporting'] = self.request.user.supporters.all

        return context
    
class AllChallengesView(ListView):
    model = Challenge
    template_name = 'challenges.html'

    def get_context_data(self, **kwargs):
        context = super(AllChallengesView, self).get_context_data(**kwargs)
        context['public_challenges'] = Instance.objects.all 
        return context

class InstanceDetailView(DetailView):
    # called from url pattern r'^go/<id>/ or some shiet like that 
    model = Instance

    def get_context_data(self, **kwargs):
        context = super(InstanceDetailView, self).get_context_data(**kwargs)
        return context


