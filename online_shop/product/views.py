
from django.shortcuts import render
from django.views import generic

from product.models import Product


# def store(request):
#     product = Product.objects.all()
#     return render(request, "product/store.html", {'Product': product})


class StoreListView(generic.ListView):
    model = Product
    template_name = "product/store.html"
    context_object_name = 'products'
