from django.test import TestCase
from .models import *
# Create your tests here.

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name='s7',
                               brand='samsung',
                               category=Category.objects.get(name="phone"),
                               description="it's a good phone",
                               image=, in_stock=,
                               price=,
                               number_in_inventory=,
                               discount=
                               )

        Product.objects.create(name=,
                               brand=,
                               category=,
                               description=,
                               image=, in_stock=,
                               price=,
                               number_in_inventory=,
                               discount=
                               )

        Product.objects.create(name=,
                               brand=,
                               category=,
                               description=,
                               image=, in_stock=,
                               price=,
                               number_in_inventory=,
                               discount=
                               )

        Product.objects.create(name=,
                               brand=,
                               category=,
                               description=,
                               image=, in_stock=,
                               price=,
                               number_in_inventory=,
                               discount=
                               )

        Product.objects.create(name=,
                               brand=,
                               category=,
                               description=,
                               image=, in_stock=,
                               price=,
                               number_in_inventory=,
                               discount=
                               )

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