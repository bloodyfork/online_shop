from django.urls import path
from product.views import store

urlpatterns = [
    path('store/', store, name="store"),
]