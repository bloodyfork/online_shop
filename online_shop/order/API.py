from django.contrib import messages
from rest_framework import generics
from .serializers import *
from product.models import Product
from customer.models import Customer
import json
from django.shortcuts import redirect
from order.models import Cart


class AddToCart(generics.CreateAPIView):
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            data = request.data
            product_id = data['ProductId']
            action = data['action']
            product = Product.objects.get(id=product_id)
            customer = Customer.objects.get(user__phone=user)

            print(action)
            print(customer)
            print(product)


# def update_cart(request):
#     user = request.user
#     if user.is_authenticated:
#         data = request.data
#         product_id = data['ProductId']
#         action = data['action']
#         product = Product.objects.get(id=product_id)
#         customer = Customer.objects.get(user__phone=user)
#
#         print(action)
#         print(customer)
#         print(product)
#         return redirect('store')
#
#     else:
#         return redirect('store')

def update_cart(request):

    data = json.loads(request.body)
    product_id = data['ProductId']
    action = data['action']
    url = request.path

    customer = request.user.customer
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(customer=customer, is_paid=False)
    order_item, created = OrderItem.objects.get_or_create(cart=cart, product=product)

    if product.add_order_item():

        if action == 'add':
            order_item.how_many += 1
            messages.info(request, "item added to your cart")
            print(url)
    elif action == 'remove':
        product.remove_order_item()
        order_item.how_many -= 1
        messages.info(request, "item was removed from your card")

    order_item.save()

    redirect('store')

    if order_item.how_many <= 0:
        order_item.delete()








