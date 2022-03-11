from rest_framework.generics import DestroyAPIView
from customer.models import Address
from customer.serializers import AddressSerializer
from order.models import OrderItem


class DeleteAPIAddress(DestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address

