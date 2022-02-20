from django.contrib import admin
from .models import *
from core.models import User
# Register your models here.
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(User)
