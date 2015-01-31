from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView

from base.models import Challenge, Instance, User, Charity

class LandingPage(TemplateView):
    template_name = "home.html"

class UserDashboard(DetailView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        
        # Get context objects.

        context['own_challenges'] = Instance.objects.filter(owner=self.request.user)
        context['challenges_in'] = self.request.user.participants_set.all()
        context['challenges_supporting'] = self.request.user.supporters_set.all()

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

        # is_friend method in User model: returns True if user is in friends
        #  context['friends_challenges'] = Challenge.objects.filter(self.request.user.is_friend(challenge__owner))

        return context

    def get(self, request):
        if not request.user.is_authenticated():
            return render_to_response('base/templates/home.html')
        else:
            return TemplateResponse(request, template_name, context)

class AddChallenge(CreateView):
    model = Challenge
    fields = ['title', 'owner', 'participant_list', 'supporter_list', 'description', ]

