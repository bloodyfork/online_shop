from django.http import HttpResponse
from rest_framework.generics import DestroyAPIView, UpdateAPIView, CreateAPIView
from rest_framework.response import Response
from customer.models import Address
from customer.serializers import AddressSerializer


class DeleteAPIAddress(DestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address


class UpdateAPIAddress(UpdateAPIView):
    serializer_class = AddressSerializer
    queryset = Address
    lookup_field = 'pk'

    def partial_update(self, request, *args, **kwargs):
        customer = request.user.customer
        data = request.data
        address = customer.address_set.get(id=data['address_id'])
        address.exact_address = data['exact_address']
        address.province = data['province']
        address.city = data['city']
        address.postal_code = data['zip']
        address.save()
        serializer = AddressSerializer(address)
        return Response(serializer.data)




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
        # ToDo make the message apear without reload
        return HttpResponse('m')
