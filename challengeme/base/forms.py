from django import forms
from django.db import models
from challengeme.base.models import Challenge, Charity, User, Instance


class ChallengeForm(forms.Form):
    class Meta:
        model = Challenge
        fields = ('title', 'description', 'charity')
     

class InstanceForm(forms.Form):
    class Meta:
        model = Instance
        fields = ('challenge', 'title', 'note', 'goal_date', 'bounty', 'participants')


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

