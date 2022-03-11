from rest_framework.generics import DestroyAPIView
from customer.models import Address
from customer.serializers import AddressSerializer


class DeleteAPIAddress(DestroyAPIView):
    serializer_class = AddressSerializer

    def get_queryset(self):

        address_id = self.request.data['the_id']
        query = Address.objects.get(id=address_id)
        return query

    def perform_destroy(self, instance):
        self.get_queryset().delete()
