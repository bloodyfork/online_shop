from django.urls import path

from product.API import ProductList
from product.views import StoreListView

urlpatterns = [
    path('store/', StoreListView.as_view(), name="store"),
    path("ListProduct/", ProductList.as_view())
]