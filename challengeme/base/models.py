from django.db import models
from django.contrib.auth.models import Challenge, Instance, User, Owner, Participant, Supporter

class Challenge(models.Model):
	owner = models.ForeignKey(User)
	
class User(models.Model):
	username = models.CharField(max_length=100)
	email = models.CharField(max_length=256)

	
