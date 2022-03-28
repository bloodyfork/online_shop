from django.contrib import messages
from rest_framework import generics, mixins
from rest_framework.response import Response

from .models import Product, Comment
from .serializers import ProductSerializer, CommentSerializer


class ProductDetailAPI(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListAPI(generics.ListAPIView, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CreateCommentAPI(generics.CreateAPIView):
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        author = request.user.customer
        context = data['context']
        product_id = data['product']
        if context == '':
            messages.info(request, 'please enter valid comment')
            return Response('serializer.data')

        else:
            product = Product.objects.get(id=product_id)
            comment = Comment.objects.create(author=author, context=context, product=product)
            comment.save()
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
