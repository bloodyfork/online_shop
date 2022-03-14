from django.urls import path
from .API import *
from order.views import cart

urlpatterns = [
    path('cart/', cart, name='cart'),


    # API
    # API
    # API
    path('AddToCart/', AddToCart.as_view(), name='AddToCart'),
    path('Update/<int:pk>', OrderItemUpdateView.as_view(), name='IncAndDec'),
    path('UpdateCartAddress/<int:pk>', CartAddressUpdateView.as_view(), name='UpdateCartAddress'),
    path('Checkout/', CheckoutAPIView.as_view(), name='Checkout'),


]
