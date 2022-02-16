from django.test import TestCase
from .models import *


# Create your tests here.

class DiscountTestCase(TestCase):
    def setUp(self):
        self.dis1 = Discount.objects.create(type="currency", value=10000)
        self.dis2 = Discount.objects.create(type="percentage", value=20, max_discount=100000)

    def test_str(self):
        self.assertEqual(str(self.dis1), '10000')


class CategoryTestCase(TestCase):
    def setUp(self):
        self.cat1 = Category.objects.create(name="Electronic Devices")

        self.cat2 = Category.objects.create(name="phone",
                                            base_category=self.cat1,
                                            )
        self.cat3 = Category.objects.create(name="laptop",
                                            base_category=self.cat1
                                            )
        self.cat4 = Category.objects.create(name="tablet",
                                            base_category=self.cat1,
                                            )

        self.cat5 = Category.objects.create(name="clothes")

        self.cat6 = Category.objects.create(name="shoes",
                                            base_category=self.cat4
                                            )
        self.cat7 = Category.objects.create(name="jackets",
                                            base_category=self.cat4
                                            )

    def test_str(self):
        self.assertEqual(str(self.cat1), "Electronic Devices")
        self.assertEqual(str(self.cat2), "phone")


class ProductTestCase(TestCase):
    def setUp(self):
        self.cat1 = Category.objects.create(name="Electronic Devices")

        self.cat2 = Category.objects.create(name="phone",
                                            base_category=self.cat1,
                                            )
        self.cat3 = Category.objects.create(name="laptop",
                                            base_category=self.cat1
                                            )
        self.cat4 = Category.objects.create(name="tablet",
                                            base_category=self.cat1,
                                            )

        self.cat5 = Category.objects.create(name="clothes")

        self.cat6 = Category.objects.create(name="jacket",
                                            base_category=self.cat4
                                            )

        self.product1 = Product.objects.create(name='s7',
                                               brand='samsung',
                                               category=self.cat2,
                                               description="it's a good phone",
                                               price=10000000,
                                               number_in_inventory=5,
                                               )

        self.product2 = Product.objects.create(name='gu603',
                                               brand='asus',
                                               category=self.cat3,
                                               description="a good laptop",
                                               in_stock=True,
                                               price=30000000,
                                               number_in_inventory=2,
                                               discount=Discount.objects.get(id=1)
                                               )

        self.product3 = Product.objects.create(name="ipad",
                                               brand="apple",
                                               category=self.cat4,
                                               description="Expensive tablet",
                                               in_stock=True,
                                               price=20000000,
                                               number_in_inventory=1,
                                               discount=Discount.objects.get(id=2)
                                               )

        self.product4 = Product.objects.create(name='jean jacket',
                                               brand="h&m",
                                               category=self.cat6,
                                               description="warm jacket",
                                               in_stock=False,
                                               price=700000,
                                               number_in_inventory=0,
                                               )

    def test_check_in_stock(self):
        self.assertEqual(self.product1.check_in_stock(), True)

    def test_after_discount_price(self):
        pass


class CommentTestCase(TestCase):
    def setUp(self):
        Comment.objects.create(context="very good", product=Product.objects.get(1))
        Comment.objects.create(context="very bad", product=Product.objects.get(2))
        Comment.objects.create(context="not bad", product=Product.objects.get(3))

    def test_str(self):
        self.assertEqual(print(Comment.objects.get(id=1)), "very good")
