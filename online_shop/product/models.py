from django.core.validators import MinValueValidator
from django.db import models
from core.models import BaseModel
from customer.models import Customer


# Create your models here.

class Product(BaseModel):
    name = models.CharField(max_length=35, unique=True, help_text="Enter name of the product ")
    brand = models.ForeignKey(to='Brand', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    description = models.TextField(max_length=500, default="Unknown")
    image = models.ImageField(blank=True, null=True, upload_to='static/images/product',
                              default='static/images/product/placeholder.png',
                              help_text="Upload photo of product here")
    in_stock = models.BooleanField(default=True)
    price = models.PositiveIntegerField(help_text="Enter price of product", validators=[MinValueValidator(0)])
    number_in_inventory = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(0)])
    discount = models.OneToOneField(to='Discount', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    def check_in_stock(self):
        if self.number_in_inventory == 0:
            self.in_stock = False
            return self.in_stock
        else:
            return self.in_stock

    def add_order_item(self):
        if self.check_in_stock():
            self.number_in_inventory -= 1
            return True
        else:
            return False

    def remove_order_item(self):
        self.number_in_inventory += 1

        return self.number_in_inventory

    def after_discount_price(self):
        if self.discount is None:
            return self.price
        elif self.discount is not None:
            if self.discount.type == "percentage":
                discount_amount = (self.price * (100 - self.discount.value)) // 100
                self.after_dis_price = discount_amount
                if discount_amount > self.discount.max_discount:
                    raise "the discount is more than maximum amount for discount"
                else:
                    res = discount_amount
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


class Brand(BaseModel):
    name = models.CharField(max_length=20, help_text="name of a brand", unique=True)
    logo = models.ImageField(upload_to="static/images/logos")

    def __str__(self):
        return f"{self.name}"


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
    author = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    context = models.CharField(max_length=180)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)

    def __str__(self):

        if self.author.user.first_name == '':
            return ' from Unknown'

        else:
            return f'from {self.author.user.first_name}'
