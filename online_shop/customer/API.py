from django.http import HttpResponse
from rest_framework.generics import DestroyAPIView, UpdateAPIView, CreateAPIView
from customer.models import Address
from customer.serializers import AddressSerializer


class DeleteAPIAddress(DestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address


class UpdateAPIAddress(UpdateAPIView):
    serializer_class = AddressSerializer
    queryset = Address
    lookup_field = 'pk'


class CreateAPIAddress(CreateAPIView):
    serializer_class = AddressSerializer
    queryset = Address

    def create(self, request, *args, **kwargs):
        postal_code = request.data['zip']
        province = request.data['province']
        city = request.data['city']
        exact_address = request.data['exact_address']
        customer = request.user.customer
        query = Address.objects.create(province=province, city=city,
                                       exact_address=exact_address,
                                       postal_code=postal_code,
                                       customer=customer)
        query.save()
        # m = messages.info(request, 'Address has been successfully created')
        return HttpResponse('m')
