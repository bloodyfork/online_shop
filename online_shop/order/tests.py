from unittest import TestCase
from order.models import *
from product.tests import Product


# Create your tests here.

class CartTestCase(TestCase):
    def setUp(self):
        Cart.objects.create(customer=Customer.objects.get(id=1))

    def test_total_price(self):
        pass

    def test_final_price(self):
        pass

    def test_check_is_paid(self):
        self.assertEqual(Cart.objects.get(id=1).check_is_paid(), False)


class OrderItemTestCase(TestCase):
    def setUp(self):
        OrderItem.objects.create(product=Product.objects.get(id=1),
                                 cart=Cart.objects.get(id=1),
                                 how_many=1
                                 )


