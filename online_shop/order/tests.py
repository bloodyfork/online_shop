from unittest import TestCase
from order.models import *
from product.tests import Product
from customer.tests import CustomerTestCase


# Create your tests here.
class OrderItemTestCase(TestCase):

class CartTestCase(TestCase):
    def setUp(self):
        Cart.objects.create(customer=Customer.objects.get(id=1))

    def test_total_price(self):
        pass

    def test_final_price(self):
        pass
