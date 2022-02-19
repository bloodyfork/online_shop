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


class CategoryBasedProductListView(generic.ListView):
    model = Product
    template_name = "product/categorybasedproduct.html"
    context_object_name = 'products'
    page_kwarg = 'pk'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "product/ProductDetail.html"
    pk_url_kwarg = "PK"
