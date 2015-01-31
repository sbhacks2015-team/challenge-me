from django.test import TestCase
from base.models import Challenge, Instance, Charity
from django.contrib.auth.models import User
import datetime
# Create your tests here.

class InstanceTestCase(TestCase):
    def setUp(self):
        d = User.objects.create_user(username="David", email="poop@berkeley.edu")
        j = User.objects.create_user(username="Jackie", email="poop2@berkeley.edu")
        charity = Charity.objects.create(name="Poops 4 Love", description="Poopy")
    
        challenge = Challenge.objects.create(title="Lose 10 Pounds", description="poopoo", owner=j, charity=charity)

        Instance.objects.create(title="Lose 10 Pounds", note="hahaha", goal_date=datetime.datetime.now()+datetime.timedelta(days=1), bounty="100.01", owner=d, challenge=challenge)

    def test_add_supporters(self):
        j = User.objects.get(name="Jackie")
        d = User.objects.get(name="David")
        instance = Instance.objects.get(title="Lose 10 Pounds")

        instance.supporters.add(d)

        self.assertTrue(d in instance.supporters.all())


