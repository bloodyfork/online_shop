from django.urls import path

from product.API import ProductListAPI
from product.views import StoreListView, CategoryListView, CategoryBasedProductListView

urlpatterns = [
    path('store/', StoreListView.as_view(), name="store"),
    path('CategoryProduct/page<int:pk>', CategoryBasedProductListView.as_view(), name="CategoryProduct"),
    path('categories/', CategoryListView.as_view(), name="categories"),

    # APIS
    # APIS
    # APIS

    path("ProductList/", ProductListAPI.as_view(), name="ProductListAPI")
]
