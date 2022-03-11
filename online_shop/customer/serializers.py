from rest_framework import serializers
from customer.models import Address


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
