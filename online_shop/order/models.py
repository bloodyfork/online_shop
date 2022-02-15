from django.db import models
from core.models import BaseModel
from customer.models import Customer
from product.models import Product
# Create your models here.


class Cart(BaseModel):
    total_price = models.PositiveIntegerField(help_text="Total Price", default=0)
    final_price = models.PositiveIntegerField(help_text="Final Price", default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    off_code = models.OneToOneField("OffCode", on_delete=models.CASCADE, null=True, blank=True)
    # status = models.ForeignKey(to=Status, on_delete=models.PROTECT)


class OrderItem(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    how_many = models.PositiveSmallIntegerField(help_text="How many of this product do you need")

    def calculate_final_price(self):
        if self.product.discount is None and \
           self.cart.off_code is None:
            self.cart.total_price += self.how_many * self.product.price
            self.cart.final_price += self.cart.total_price

        elif self.product.discount is None and \
                self.cart.off_code is not None:


class OffCode(BaseModel):
    the_code = models.CharField(max_length=10, help_text="Enter code for offer")
    value = models.PositiveIntegerField(help_text="Enter code percentage for offer")
    is_active = models.BooleanField(default=True)
    how_many_use = models.PositiveSmallIntegerField(default=3, help_text="how many times do you want this code")


# class status:
#     title = models.CharField(choices=)
