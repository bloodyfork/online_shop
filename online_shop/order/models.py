from django.db import models
from core.models import BaseModel
from customer.models import Customer
# Create your models here.


class Cart(BaseModel):
    total_price = models.PositiveIntegerField(help_text="Total Price", default=0)
    final_price = models.PositiveIntegerField(help_text="Final Price", default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # off_code = models.OneToOneField(OffCode, on_delete=models.CASCADE, null=True, blank=True)

class OrderItem(BaseModel):
    pass