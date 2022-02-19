from django.core.validators import MinValueValidator
from django.db import models
from core.models import BaseModel


# Create your models here.

class Product(BaseModel):
    name = models.CharField(max_length=25, unique=True, help_text="Enter name of the product ")
    brand = models.CharField(max_length=18, help_text="Enter brand of product")
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    description = models.CharField(max_length=100, )
    image = models.ImageField(blank=True, null=True, upload_to='static/images',
                              help_text="Upload photo of product here")
    in_stock = models.BooleanField(default=True)
    price = models.PositiveIntegerField(help_text="Enter price of product")
    number_in_inventory = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])
    discount = models.OneToOneField(to='Discount', on_delete=models.SET_NULL, blank=True, null=True)

    def check_in_stock(self):
        if self.number_in_inventory == 0:
            self.in_stock = False
        else:
            pass

    def after_discount_price(self):
        if self.discount is None:
            return self.price
        elif self.discount is not None:
            if self.discount.type == "percentage":
                discount_amount = (self.price * self.discount.value) // self.price
                if discount_amount > self.discount.max_discount:
                    raise "the discount is more than maximum amount for discount"
                else:
                    res = self.price - discount_amount
                    return res

            elif self.discount.type == "currency":
                if self.discount.value >= self.price:
                    raise "the discount is higher than price"
                else:
                    res = self.price - self.discount.value
                    return res

            else:
                raise "Error while precessing logic"
        else:
            raise "Error while precessing logic"


class Category(BaseModel):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=20, unique=True, help_text="Enter name of category")
    base_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Discount(BaseModel):
    type = models.CharField(choices=[("percentage", "percentage"), ("currency", "currency")], max_length=10,
                            help_text="choose type of discount")
    value = models.PositiveIntegerField()
    max_discount = models.PositiveIntegerField(help_text="Enter max amount of discount", null=True, blank=True)

    def __str__(self):
        return f"{self.value} {self.type}"


class Comment(BaseModel):
    context = models.CharField(max_length=120)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
