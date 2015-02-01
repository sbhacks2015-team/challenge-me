from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.forms.models import modelform_factory, modelformset_factory
from challengeme.base.forms import NameForm, ChallengeForm, InstanceForm
from challengeme.base.models import Challenge, Instance, User, Charity, Profile


class LandingPage(TemplateView):
    template_name = "home.html"


def new_challenge(request):
    #import pdb; pdb.set_trace()
    if request.method == "POST":
        ChallengeFormSet = modelform_factory(Challenge)
        cform = ChallengeFormSet(request.POST)
        if cform.is_valid():
            new_challenge = cform.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        ChallengeFormSet = modelform_factory(Challenge)
        cform = ChallengeFormSet()
        
    return render(request, "new_challenge.html", {'cform': cform})

def test_form(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')
    else:
        form = NameForm()

    return render(request, 'testform.html', {'form': form})
    def get_context_data(self, **kwargs):
        context = super(TestCreate, self).get_context_data(**kwargs)
        context['cform'] = ChallengeForm()
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

def poop(request):
    now = datetime.datetime.now()
    html = "<html>sup bae it's %s</html>" % now
    return HttpResponse(html)
