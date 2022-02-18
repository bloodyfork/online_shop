from django.urls import path

from order.views import cart

urlpatterns = [
    path('cart/', cart, name='cart'),

]
