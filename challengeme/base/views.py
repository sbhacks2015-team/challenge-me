from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.http import HttpResponse
import datetime
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from challengeme.base.forms import ChallengeForm, InstanceForm
from challengeme.base.models import Challenge, Instance, User, Charity, Profile


class LandingPage(TemplateView):
    template_name = "home.html"


def poop(request):
    now = datetime.datetime.now()
    html = "<html>sup bae it's %s</html>" % now
    return HttpResponse(html)

def add_own_instance(request):
    if request.method == "POST":
        form = ChallengeForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/dashboard/')
    else:
        form = ChallengeForm(request.POST)

    return render(request, 'testcreate.html', {'form': form})


class TestCreate(TemplateView):
    template_name = "testview.html"
    
    def get_context_data(self, **kwargs):
        context = super(TestCreate, self).get_context_data(**kwargs)
        return context

class UserDashboard(ListView):
    model = Instance
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(UserDashboard, self).get_context_data(**kwargs)
        # Get context objects.
        context['own_challenges'] = Instance.objects.filter(owner=self.request.user)
        context['challenges_participating'] = self.request.user.participants.all()
        context['challenges_supporting'] = self.request.user.supporters.all()
        return context
    
class AllChallengesView(ListView):
    model = Challenge
    template_name = 'challenges.html'

    def get_context_data(self, **kwargs):
        context = super(AllChallengesView, self).get_context_data(**kwargs)
        context['public_challenges'] = Challenge.objects.all 
        return context


class ChallengeDetailView(DetailView):
    model = Challenge
    template_name = "challenge_detail.html"    

    def get_context_data(self, **kwargs):
        context = super(ChallengeDetailView, self).get_context_data(**kwargs)
        return context


class InstanceDetailView(DetailView):
    model = Instance
    template_name = "instance_detail.html"

    def get_context_data(self, **kwargs):
        context = super(InstanceDetailView, self).get_context_data(**kwargs)
        return context

