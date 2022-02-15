from django.db import models
from core.models import BaseModel
from customer.models import Customer
from product.models import Product
# Create your models here.


class Cart(BaseModel):
    total_price = models.PositiveIntegerField(help_text="Total Price", default=0)
    final_price = models.PositiveIntegerField(help_text="Final Price", default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # status = models.ForeignKey(to=Status, on_delete=models.PROTECT)
    # off_code = models.OneToOneField(OffCode, on_delete=models.CASCADE, null=True, blank=True)


class OrderItem(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    how_many = models.PositiveSmallIntegerField(help_text="How many of this product do you need")


# class status:
#     title = models.CharField(choices=)

# class OffCode(BaseModel):
#     pass