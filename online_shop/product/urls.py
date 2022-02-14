from django.urls import path
from product.views import store

urlpatterns = [
    path('', store, name="store"),
]