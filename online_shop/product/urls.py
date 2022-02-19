from django.urls import path

from product.API import ProductListAPI
from product.views import StoreListView, CategoryListView, CategoryBasedProductListView, ProductDetailView

urlpatterns = [
    path('store/', StoreListView.as_view(), name="store"),
    path('CategoryProduct/page<int:pk>', CategoryBasedProductListView.as_view(), name="CategoryProduct"),
    path('categories/', CategoryListView.as_view(), name="categories"),
    path('ProductDetail/', ProductDetailView.as_view(), name='ProductDetail'),

    # APIS
    # APIS
    # APIS

    path("ProductList/", ProductListAPI.as_view(), name="ProductListAPI")
]
