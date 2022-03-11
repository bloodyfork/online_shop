from rest_framework.generics import DestroyAPIView, UpdateAPIView
from customer.models import Address
from customer.serializers import AddressSerializer


class DeleteAPIAddress(DestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address


class UpdateAPIAddress(UpdateAPIView):
    serializer_class = AddressSerializer
    queryset = Address
    lookup_field = 'pk'
