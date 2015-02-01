from django.test import TestCase
from challengeme.base.models import Challenge, Instance, Charity
from django.contrib.auth.models import User
import datetime
# Create your tests here.

class InstanceTestCase(TestCase):
    def setUp(self):
        d = User.objects.create_user(username="David", email="poop@berkeley.edu")
        j = User.objects.create_user(username="Jackie", email="poop2@berkeley.edu")
        m = User.objects.create_user(username="Max", email="poop3@berkeley.edu")

        charity = Charity.objects.create(name="Poops 4 Love", description="Poopy")

        challenge = Challenge.objects.create(title="Lose 10 Pounds", description="poopoo", owner=j, charity=charity)

        Instance.objects.create(title="Lose 10 Pounds", note="hahaha", goal_date=datetime.datetime.now()+datetime.timedelta(days=1), bounty="100.01", owner=d, challenge=challenge)

    def test_add_supporters(self):
        j = User.objects.get(username="Jackie")
        d = User.objects.get(username="David")
        m = User.objects.get(username="Max")
        instance = Instance.objects.get(title="Lose 10 Pounds")

        instance.supporters.add(d)
        instance.supporters.add(m)

        self.assertTrue(m in instance.supporters.all())
        self.assertTrue(d in instance.supporters.all())

    def test_add_participants(self):
        j = User.objects.get(username="Jackie")
        d = User.objects.get(username="David")
        m = User.objects.get(username="Max")
        instance = Instance.objects.get(title="Lose 10 Pounds")

        instance.participants.add(d)
        instance.participants.add(m)

        self.assertTrue(m in instance.participants.all())
        self.assertTrue(d in instance.participants.all())

    def test_get_instance_from_participant(self):
        j = User.objects.get(username="Jackie")
        d = User.objects.get(username="David")
        m = User.objects.get(username="Max")
        instance = Instance.objects.get(title="Lose 10 Pounds")

        instance.participants.add(d)
        instance.participants.add(m)

        self.assertTrue(d.participants.get(title="Lose 10 Pounds") == instance)

    def test_get_instance_from_owner(self):
        j = User.objects.get(username="Jackie")
        d = User.objects.get(username="David")
        m = User.objects.get(username="Max")
        instance = Instance.objects.get(title="Lose 10 Pounds")

        instance.participants.add(d)
        instance.participants.add(m)

        self.assertTrue(Instance.objects.get(title="Lose 10 Pounds") == Instance.objects.filter(owner=d)[0])
