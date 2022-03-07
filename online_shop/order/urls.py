from django.urls import path
from .API import *
from order.views import cart

urlpatterns = [
    path('cart/', cart, name='cart'),


    # API
    # API
    # API
    path('AddToCart/', AddToCart.as_view(), name='AddToCart'),
    # path('AddToCart/', update_cart, name='AddToCart'),

]
