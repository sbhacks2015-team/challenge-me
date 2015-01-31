from django.db import models
from django.contrib.auth.models import Challenge, Instance, User, Charity

class Challenge(models.Model):
	owner = models.ForeignKey(User)
	charity = models.ForeignKey(Charity)


class Instance(models.Model):
	owner = models.ForeignKey(User)
	challenge = models.ForeignKey(Challenge)
	participants = models.ManyToMany(User)
	supporters = models.ManyToMany(User)


class User(models.Model):
	username = models.CharField(max_length=100)
	email = models.CharField(max_length=256)


class Charity(models.Model):
	name = models.CharField(max_length=256)
	description = models.CharField()
