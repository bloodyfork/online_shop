from rest_framework import generics
from .serializers import *


class AddToCart(generics.CreateAPIView):
    serializer_class = CartSerializer
