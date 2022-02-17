from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    car_set = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Product

# class productSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=25,)
#     brand = serializers.CharField(max_length=18)
#     category = CategorySerializer(read_only=True)
#     description = serializers.CharField(max_length=100, )
#     image = serializers.ImageField(blank=True, null=True, upload_to='media/product',
#                               help_text="Upload photo of product here")
#     in_stock = serializers.BooleanField(default=True)
#     price = serializers.PositiveIntegerField(help_text="Enter price of product")
#     number_in_inventory = serializers.IntegerField()
#     discount = serializers.On
#
#     def update(self, instance: Product, validated_data: dict) -> Product:
#         instance.brand = validated_data.get('brand', instance.brand)
#         instance.acceleration = validated_data.get('acceleration', instance.acceleration)
#         instance.color = validated_data.get('color', instance.color)
#         return instance
#
#     def create(self, validated_data: dict) -> Product:
#         return Product.objects.create(**validated_data)
