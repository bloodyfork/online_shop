from django.contrib import admin
from .models import *
from core.models import User
# Register your models here


class AddressShow(admin.ModelAdmin):
    list_display = ['customer', 'province', 'city', 'postal_code', 'exact_address']


admin.site.register(Customer)
admin.site.register(Address, AddressShow)
admin.site.register(User)
