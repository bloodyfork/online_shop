from django.urls import path

from product.API import ProductList
from product.views import store

urlpatterns = [
    path('store/', store, name="store"),
    path("listProduct/", ProductList.as_view())
]