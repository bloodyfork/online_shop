from django.contrib import admin
from .models import *
# Register your models here.


class CartShow(admin.ModelAdmin):
    list_display = ['customer']


class OrderItemShow(admin.ModelAdmin):
    list_display = ['product', 'how_many', 'cart']


admin.site.register(Cart, CartShow)
admin.site.register(OffCode)
admin.site.register(OrderItem, OrderItemShow)
