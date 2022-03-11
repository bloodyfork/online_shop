from django.contrib import messages
from rest_framework import generics
from .serializers import *
from product.models import Product
from customer.models import Customer
from order.models import Cart
from rest_framework.response import Response
from django.shortcuts import HttpResponse


class AddToCart(generics.CreateAPIView):
    serializer_class = OrderItemSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        if user.is_authenticated:

            product_id = data['ProductId']

            product = Product.objects.get(id=product_id)
            customer = Customer.objects.get(user__phone=user)
            cart, created = Cart.objects.get_or_create(customer=customer, is_paid=False)
            cart_objects = cart.orderitem_set.all()

            item_list = []
            for items in cart_objects:
                item_list.append(items.product.name)

            if product.name in item_list:

                m = messages.warning(request, 'Product already exists in your cart!')
                return HttpResponse(m)

            else:
                messages.info(request, 'Item added to your cart!')
                order_item, created = OrderItem.objects.create(cart=cart, product=product, how_many=1)
                order_item.save()
                serializer = OrderItemSerializer(order_item)
                serializer.save()
                return Response(serializer.data)
        else:
            pass
            # ToDO make it for not registered users


class OrderItemUpdateView(generics.UpdateAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
