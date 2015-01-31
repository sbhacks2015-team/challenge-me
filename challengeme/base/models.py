a
from django.db import models
from django.contrib.auth.models import Challenge, Instance, User, Charity

class Challenge(models.Model):
	context_id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=256)
	description = models.CharField(max_length=60000)

	owner = models.ForeignKey(User)
	charity = models.ForeignKey(Charity)


class Instance(models.Model):
        title = models.CharField(max_length=256)
	context_id = models.IntegerField(primary_key=True)
	note = models.CharField(max_length=60000)
	release_date = models.DateField(auto_now_add=True)
	goal_date = models.DateField()
	bounty = models.DecimalField(max_digits=4, decimal_places=8)

	owner = models.ForeignKey(User)
	challenge = models.ForeignKey(Challenge)
	participants = models.ManyToMany(User, related_name="participants")
	supporters = models.ManyToMany(User, related_name="supporters")


class User(models.Model):
	context_id = models.IntegerField(primary_key=True)
	username = models.CharField(max_length=100)
	email = models.CharField(max_length=256)


class Charity(models.Model):
	context_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=256)
	description = models.CharField(max_length=60000)
