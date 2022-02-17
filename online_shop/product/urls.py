from django.urls import path
from product.views import store, ProductList

urlpatterns = [
    path('store/', store, name="store"),
    path("listProduct/", ProductList.as_view())
]