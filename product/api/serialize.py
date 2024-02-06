from rest_framework import serializers
from product.models import *
from category.models import *


# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     email = serializers.EmailField()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'email']

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()
    image = serializers.ImageField()
    count = serializers.IntegerField()
    createdat = serializers.DateTimeField(read_only=True)
    updatedat = serializers.DateTimeField(read_only=True)
    category = CategorySerializer(allow_null=True)