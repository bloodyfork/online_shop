from django.db import models
from core.models import BaseModel


# Create your models here.

class Product(BaseModel):
    name = models.CharField(max_length=25, unique=True, help_text="Enter name of the product ")
    brand = models.CharField(max_length=18, help_text="Enter brand of product")
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    description = models.CharField(max_length=100, )
    image = models.ImageField(upload_to='media/product', help_text="Upload photo of product here")
    in_stock = models.BooleanField(default=True)
    price = models.PositiveIntegerField(help_text="Enter price of product")
    number_in_inventory = models.PositiveSmallIntegerField(default=1)
    discount = models.OneToOneField(to='Discount', on_delete=models.CASCADE)

    def check_in_stock(self):
        if self.number_in_inventory == 0:
            self.in_stock = False
        else:
            pass


class Category(BaseModel):
    name = models.CharField(max_length=20, unique=True, help_text="Enter name of category")
    base_category = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Discount(BaseModel):
    type = models.CharField(choices=[("percentage", "percentage"), ("currency", "currency")], max_length=10,
                            help_text="choose type of discount")
    value = models.PositiveIntegerField()
    max_discount = models.PositiveIntegerField(blank=True, null=True, help_text="Enter max amount of discount")

    def __str__(self):
        return f"{self.value} {self.type}"


class Comment(BaseModel):
    context = models.CharField(max_length=120)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)