from django.contrib.auth.models import User
from django.db import models
from core.models import BaseModel
# Create your models here.


class Customer(BaseModel):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14, help_text="Enter your phone number")

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

    def __str__(self):
        return f'{self.province, self.city, self.exact_address}'