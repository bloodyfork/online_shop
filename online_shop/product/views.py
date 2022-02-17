from django.shortcuts import render
from rest_framework import mixins, generics
from product.models import Product
from .serializers import ProductSerializer


def store(request):
    context = {}
    return render(request, "product/store.html", context)


class ProductDetail(generics.RetrieveDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductList(generics.ListAPIView, mixins.ListModelMixin):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)