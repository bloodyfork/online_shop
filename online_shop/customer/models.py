from django.contrib.auth.models import User
from django.db import models
from core.models import BaseModel
# Create your models here.


class Customer(BaseModel):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14, help_text="Enter your phone number")
    address = ...


class Address(BaseModel):
    province = models.CharField(max_length=18, help_text="Enter your address")
    city = models.CharField(max_length=18, help_text="Enter your address")
    exact_address = models.CharField(max_length=100, help_text="Enter your exact address")
    postal_code = models.PositiveIntegerField(max_length=30, blank=True, null=True)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)