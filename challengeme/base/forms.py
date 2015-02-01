from django import forms
from django.db import models


class ChallengeForm(form.Form):
    title = models.CharField(blank=False, max_length=256)
    description = models.CharField(max_length=60000)
    charity = models.ForeignKey(Charity)
    
    def __str__(self):
        return "(Form)"+self.title


class InstanceForm(form.Form):
    challenge = models.ForeignKey(Challenge)
    title = models.CharField(max_length=60000)
    note = models.CharField(max_length=60000)
    goal_date = models.DateFIeld()
    bounty = models.DecimalField(blank=False, default=0.0, max_digits=14, decimal_places=8)
    participants = models.ManyToManyField(User, related_name="participants")

    def __str__(self):
        return "(Form)"+self.title


