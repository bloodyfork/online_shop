from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from .serializers import *
from product.models import Product
from customer.models import Customer
from order.models import Cart
from rest_framework.response import Response
from django.shortcuts import HttpResponse, redirect


# API for OrderItems Create Update Delete
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
    queryset = OrderItem

    def partial_update(self, request, *args, **kwargs):
        data = request.data
        item = OrderItem.objects.get(id=data['item_id'])

        if data['action'] == 'increase':

            if item.product.number_in_inventory >= item.how_many + 1:
                item.how_many += 1
                item.save()
                serializer = OrderItemSerializer(item)
                return Response(serializer.data)
            else:
                messages.info(request, "No more of this product is in in inventory")
                return Response('s')

        elif data['action'] == 'decrease':
            if item.how_many - 1 != 0:
                item.how_many -= 1
                item.save()
                serializer = OrderItemSerializer(item)
                return Response(serializer.data)
            else:
                item.delete()
                return HttpResponse('Request not found')

        else:
            return HttpResponse('Request not found')


# API for cart Update
class CartAddressUpdateView(generics.UpdateAPIView, LoginRequiredMixin):
    serializer_class = CartSerializer
    queryset = Cart

    def partial_update(self, request, *args, **kwargs):
        customer = request.user.customer
        address_id = request.data['address']
        the_cart = customer.cart_set.get(is_paid=False)
        the_address = customer.address_set.get(id=address_id)
        the_cart.address = the_address
        the_cart.save()
        serializer = CartSerializer(the_cart)
        return Response(serializer.data)


class CheckoutAPIView(generics.UpdateAPIView):
    serializer_class = CartSerializer
    queryset = Cart

    def partial_update(self, request, *args, **kwargs):
        customer = request.user.customer
        cart_id = request.data['cart_id']
        the_cart = customer.cart_set.get(id=cart_id)
        order_items = the_cart.orderitem_set.all()

        if the_cart.address is not None:
            the_cart.is_paid = True
            the_cart.save()
            for o in order_items:
                productz = o.product
                productz.number_in_inventory -= o.how_many
                productz.save()

            serializer = CartSerializer(the_cart)
            messages.info(request, 'Order Successfully paid')
            return Response(serializer.data)

        else:
            messages.info(request, 'You should choose an address')
            serializer = CartSerializer(the_cart)
            return Response(serializer.data)

