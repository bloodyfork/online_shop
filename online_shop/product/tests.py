from django.test import TestCase
from .models import *


# Create your tests here.

class DiscountTestCase(TestCase):
    def setUp(self):
        Discount.objects.create(type="currency", value=10000)
        Discount.objects.create(type="percentage", value=20, max_discount=100000)


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="Electronic Devices")
        Category.objects.create(name="phone",
                                base_category=Category.objects.get(name="Electronic Devices")
                                )

        Category.objects.create(name="laptop",
                                base_category=Category.objects.get(name="Electronic Devices")
                                )

        Category.objects.create(name="tablet",
                                base_category=Category.objects.get(name="Electronic Devices")
                                )

        Category.objects.create(name="clothes")
        Category.objects.create(name="shoes",
                                base_category=Category.objects.get(name="clothes")
                                )
        Category.objects.create(name="jackets",
                                base_category=Category.objects.get(name="clothes")
                                )

    def test_str(self):
        self.assertEqual(print(Category.objects.get(id=1)), "Electronic Devices")


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name='s7',
                               brand='samsung',
                               category=Category.objects.get(name="phone"),
                               description="it's a good phone",
                               price=10000000,
                               number_in_inventory=5,
                               discount=None
                               )

        Product.objects.create(name='gu603',
                               brand='asus',
                               category=Category.objects.get(name="laptop"),
                               description="a good laptop",
                               in_stock=True,
                               price=30000000,
                               number_in_inventory=2,
                               discount=Discount.objects.get(id=1)
                               )

        Product.objects.create(name="ipad",
                               brand="apple",
                               category=Category.objects.get(name="tablet"),
                               description="Expensive tablet",
                               in_stock=True,
                               price=20000000,
                               number_in_inventory=1,
                               discount=Discount.objects.get(id=2)
                               )

        Product.objects.create(name='jean jacket',
                               brand="h&m",
                               category=Category.objects.get(name="jacket"),
                               description="warm jacket",
                               in_stock=False,
                               price=700000,
                               number_in_inventory=0,
                               discount=None
                               )

    def test_check_in_stock(self):
        pass

    def test_after_discount_price(self):
        pass



