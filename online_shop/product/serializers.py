from rest_framework import serializers
from product.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    car_set = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
