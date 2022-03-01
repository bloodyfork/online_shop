from rest_framework import generics
from .serializers import *
from product.models import Product



class AddToCart(generics.CreateAPIView):
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)

        user = request.user
        product = Product.objects.get()