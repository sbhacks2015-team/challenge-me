from django.db import models
from django.contrib.auth.models import Challenge, User, Charity, Instance, Owner, Participant, Supporter

class Challenge(models.Model):
	owner = models.ForeignKey(User)

	
class User(models.Model):
	username = models.CharField(max_length=100)
	email = models.CharField(max_length=256)


class Charity(models.Model):
	pass


class Instance(models.Model):
	pass


class Owner(models.Model):
	pass


class Participant(models.Model):
	pass


class Supporter(models.Model):
	pass

	
