from django.contrib import messages
from rest_framework import generics
from .serializers import *
from product.models import Product
from customer.models import Customer
from order.models import Cart
from rest_framework.response import Response
# import json
# from django.shortcuts import redirect


class AddToCart(generics.CreateAPIView):
    serializer_class = OrderItemSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        if user.is_authenticated:

            product_id = data['ProductId']
            action = data['action']

            product = Product.objects.get(id=product_id)
            customer = Customer.objects.get(user__phone=user)
            cart, created = Cart.objects.get_or_create(customer=customer, is_paid=False)
            cart_objects = cart.orderitem_set.all()

            item_list = []
            for items in cart_objects:
                item_list.append(items.product.name)

            if product.name in item_list:
                messages.warning(request, 'Product already exists in your cart!')

            else:
                messages.info(request, 'Item added tp your cart!')
                order_item, created = OrderItem.objects.create(cart=cart, product=product, how_many=1)
                order_item.save()
                serializer = OrderItemSerializer(order_item)
                serializer.save()
                return Response(serializer.data)
        else:
            pass
            # ToDO make it for not registered users




# def update_cart(request):
#
#     data = json.loads(request.body)
#     product_id = data['ProductId']
#     action = data['action']
#     # url = request.path
#
#     customer = request.user.customer
#     product = Product.objects.get(id=product_id)
#     cart, created = Cart.objects.get_or_create(customer=customer, is_paid=False)
#     order_item, created = OrderItem.objects.get_or_create(cart=cart, product=product)
#
#     if product.add_order_item():
#
#         if action == 'add':
#             order_item.how_many += 1
#             messages.info(request, "item added to your cart")
#
#     elif not product.add_order_item():
#         messages.info(request, 'Product is out of stock')
#
#     elif action == 'remove':
#         product.remove_order_item()
#         order_item.how_many -= 1
#         messages.info(request, "item was removed from your card")
#         return redirect('store')
#
#     order_item.save()
#
#     if order_item.how_many <= 0:
#         order_item.delete()








