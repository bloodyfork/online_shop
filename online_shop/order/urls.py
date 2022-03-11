from django.urls import path, include
from .API import *
from order.views import cart

urlpatterns = [
    path('cart/', cart, name='cart'),


    # API
    # API
    # API
    path('AddToCart/', AddToCart.as_view(), name='AddToCart'),
    path('Update/<int:pk>', OrderItemUpdateView.as_view(), name='IncAndDec'),
    # path('AddToCart/', update_cart, name='AddToCart'),

]
