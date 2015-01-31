from django.db import models
from django.contrib.auth.models import User

class Charity(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=60000)
    bitcoin_address = models.CharField(min_length=26, max_length=35)


class Challenge(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=60000)
    owner = models.ForeignKey(User)
    charity = models.ForeignKey(Charity)


class Instance(models.Model):
    title = models.CharField(max_length=256)
    note = models.CharField(max_length=60000)
    release_date = models.DateField(auto_now_add=True)
    goal_date = models.DateField()
    bounty = models.DecimalField(max_digits=14, decimal_places=8)

    owner = models.ForeignKey(User)
    challenge = models.ForeignKey(Challenge)
    participants = models.ManyToManyField(User, related_name="participants")
    supporters = models.ManyToManyField(User, related_name="supporters")



