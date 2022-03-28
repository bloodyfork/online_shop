from django.contrib import admin
from .models import *
# Register your models here.


class CartShow(admin.ModelAdmin):
    list_display = ['customer', 'total_price', 'final_price', 'is_paid', 'is_deleted']


class OrderItemShow(admin.ModelAdmin):
    list_display = ['product', 'how_many', 'cart']


class OffCodeShow(admin.ModelAdmin):
    list_display = ['the_code', 'is_active', 'how_many_use']


admin.site.register(Cart, CartShow)
admin.site.register(OffCode)
admin.site.register(OrderItem, OrderItemShow)
