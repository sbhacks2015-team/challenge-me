from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Charity(models.Model):
    name = models.CharField(blank=False, max_length=256)
    email = models.EmailField(max_length=254)
    description = models.CharField(max_length=60000)
    #TODO: add min_length
    #bitcoin_address = models.CharField(min_length=26, max_length=35)
    bitcoin_address = models.CharField(max_length=35)
    balance = models.DecimalField(default=0.00000000, max_digits=14, decimal_places=8)

    def __str__(self):
        return self.name


class Challenge(models.Model):
    title = models.CharField(blank=False, max_length=256)
    description = models.CharField(max_length=60000)
    owner = models.ForeignKey(User)
    charity = models.ForeignKey(Charity)
    
    def __str__(self):
        return self.title


class Instance(models.Model):
    challenge = models.ForeignKey(Challenge)
    #TODO: add default title parameter
    # default_title = challenge.title
    # title = models.CharField(blank=False, default=default_title, max_length=256)
    title = models.CharField(blank=False, max_length=256)
    note = models.CharField(max_length=60000)
    release_date = models.DateField(auto_now_add=True)
    goal_date = models.DateField()
    bounty = models.DecimalField(blank=False, default=0.0, max_digits=14, decimal_places=8)
    balance = models.DecimalField(default=0.00000000, max_digits=14, decimal_places=8)
    #TODO can't divide DecimalField s
    # percentage = models.DecimalField(balance.__float__() / bounty.__float__() or "No bounty!", max_digits=14, decimal_places=8)
    owner = models.ForeignKey(User)
    participants = models.ManyToManyField(User, related_name="participants")
    supporters = models.ManyToManyField(User, related_name="supporters")
    
    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    balance = models.DecimalField(default=0.00000000, max_digits=14, decimal_places=8)
    bitcoin_address = models.CharField(max_length=35)
    first_name = models.CharField(blank=False, default="null", max_length=30)
    last_name = models.CharField(blank=False, default="null", max_length=40)
    email = models.EmailField(blank=False, default="null", max_length=254)

    def __str__(self):
        return "Profile for %s" % str(self.user)

class NameForm(forms.Form):
    your_name = forms.CharField(label="You name", max_length=100)

class ChallengeForm(ModelForm):
    class Meta:
        model = Challenge
        fields = ['title', 'description', 'charity']


class InstanceForm(ModelForm):
    class Meta:
        model = Instance
        fields = ['challenge', 'title', 'note', 'goal_date', 'bounty', 'participants',]


