from django.db import models

# Create your models here.

class Challenge(models.Model):
	owner = models.ForeignKey(User)
	
class User(models.Model):
	username = models.CharField(max_length=100)
	email = models.CharField(max_length=256)

	
