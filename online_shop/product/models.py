from django.db import models
from core.models import BaseModel


# Create your models here.

class Product(BaseModel):
    name = models.CharField(max_length=25, unique=True, help_text="Enter name of the product ")
    category = ...  ###################################################################### ToDo FK --> Category
    brand = models.CharField(max_length=18, help_text="Enter brand of product")
    image = models.ImageField(upload_to=..., help_text="Upload photo of product here")  # ToDo make upload work,SetMedia
    price = models.PositiveIntegerField(help_text="Enter price of product")
    description = models.CharField(max_length=100, )
    in_stock = models.BooleanField(default=True)
    number_in_inventory = models.PositiveSmallIntegerField()
    discount = ...  #################################################################### ToDo FK --> Discount
