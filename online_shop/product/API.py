from rest_framework import generics, mixins

from .models import Product
from .serializers import ProductSerializer


class ProductDetailAPI(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListAPI(generics.ListAPIView, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CreateCommentAPI(generics.CreateAPIView):
    serializer_class = ...
