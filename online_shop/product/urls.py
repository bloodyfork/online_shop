from django.urls import path

from product.API import ProductListAPI
from product.views import StoreListView, CategoryListView

urlpatterns = [
    path('store/', StoreListView.as_view(), name="store"),
    path('categories/', CategoryListView.as_view(), name="categories"),
    path("ProductList/", ProductListAPI.as_view(), name="ProductListAPI")
]