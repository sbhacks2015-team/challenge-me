from django import forms
from django.db import models
from challengeme.base.models import Challenge, Charity, User


class ChallengeForm(forms.Form):
    title = models.CharField(blank=False, max_length=256)
    description = models.CharField(max_length=60000)
    charity = models.ForeignKey(Charity)
    

class InstanceForm(forms.Form):
    challenge = models.ForeignKey(Challenge)
    title = models.CharField(max_length=60000)
    note = models.CharField(max_length=60000)
    goal_date = models.DateField()
    bounty = models.DecimalField(blank=False, default=0.0, max_digits=14, decimal_places=8)
    participants = models.ManyToManyField(User, related_name="participants")

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

