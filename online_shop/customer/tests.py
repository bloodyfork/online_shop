from unittest import TestCase
from django.contrib.auth.models import User
from customer.models import Customer
# Create your tests here.


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="akbar", password="HeyYou1234")


class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(user=User.objects.get(
            username="akbar"),
            customer__phone="09338616475")
