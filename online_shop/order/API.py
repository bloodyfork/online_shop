from rest_framework import generics
from .serializers import *
from product.models import Product
from core.models import User

class AddToCart(generics.CreateAPIView):
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            data = request.data
            product_id = data['ProductId']
            action = data['action']
            product = Product.objects.get(id=product_id)
            get_user = User.objects.get(phone=user)

            print(action)
            print(get_user)
            print(product)


# def updateItem(request):
#     return JsonResponse('added the item', safe=False)
