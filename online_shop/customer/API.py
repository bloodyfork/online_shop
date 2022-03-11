from rest_framework.generics import DestroyAPIView
from serializers import AddressSerializer


class DeleteAPIAddress(DestroyAPIView):
    serializer_class = AddressSerializer
    lookup_url_kwarg = None
