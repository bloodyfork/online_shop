from rest_framework import serializers
from product.models import Category, Product, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    car_set = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
