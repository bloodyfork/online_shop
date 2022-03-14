from django.contrib import admin
from .models import *


# Register your models here.


class CategoryShow(admin.ModelAdmin):
    list_display = ('name', 'base_category')
    list_filter = ['name']


class ProductShow(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'category', 'in_stock', 'number_in_inventory']
    list_filter = ['name']


class BrandShow(admin.ModelAdmin):
    list_display = ('name', 'logo')
    list_filter = ['name']


admin.site.register(Product, ProductShow)
admin.site.register(Category, CategoryShow)
admin.site.register(Discount)
admin.site.register(Comment)
admin.site.register(Brand, BrandShow)
