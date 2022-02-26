from rest_framework import serializers
from order.models import OrderItem


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
