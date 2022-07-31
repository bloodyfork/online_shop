from rest_framework import serializers
from customer.models import Address
from order.models import Cart
from core.models import User


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
