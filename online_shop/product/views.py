from django.views import generic
from product.models import Product, Category


class StoreListView(generic.ListView):
    model = Product
    template_name = "product/store.html"
    context_object_name = 'products'


class CategoryListView(generic.ListView):
    model = Category
    template_name = "product/categories.html"
    context_object_name = 'category'
