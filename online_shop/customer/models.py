from core.models import User
from django.db import models
from core.models import BaseModel
from order.models import Cart


class Customer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Address(BaseModel):
    class Meta:
        verbose_name_plural = "addresses"

    province = models.CharField(max_length=18, help_text="Enter your address")
    city = models.CharField(max_length=18, help_text="Enter your address")
    exact_address = models.CharField(max_length=100, help_text="Enter your exact address")
    postal_code = models.PositiveIntegerField(blank=True, null=True)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.province, self.city, self.exact_address}'