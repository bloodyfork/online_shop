
from django.shortcuts import render
from django.views import generic

from product.models import Product

class StoreListView(generic.ListView):
    model = Product
    template_name = "product/store.html"
    context_object_name = 'products'
