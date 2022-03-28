from django.urls import path

from product.API import ProductListAPI, CreateCommentAPI
from product.views import StoreListView, CategoryListView, CategoryBasedProductListView, ProductDetailView, FrontCategories

urlpatterns = [
    path('store/', StoreListView.as_view(), name="store"),
    # path('CategoryProduct/<slug:slug>', CategoryBasedProductListView.as_view(), name="CategoryProduct"),
    path('CategoryProduct/<slug:slug>', FrontCategories.as_view(), name="CategoryProduct"),
    path('categories/', CategoryListView.as_view(), name="categories"),
    path('ProductDetail/<int:pk>', ProductDetailView.as_view(), name='ProductDetail'),

    # APIS
    # APIS
    # APIS

    path("ProductListAPI/", ProductListAPI.as_view(), name="ProductListAPI"),
    path("CommentCreateAPI/", CreateCommentAPI.as_view(), name="CreateCommentAPI")
]
