from rest_framework import serializers
from product.models import *
from category.models import *
from rest_framework.validators import UniqueValidator


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
    name = serializers.CharField(max_length=100,validators=[UniqueValidator(queryset=Product.objects.all())])
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()
    image = serializers.ImageField(allow_empty_file=True)
    count = serializers.IntegerField()
    createdat = serializers.DateTimeField(read_only=True)
    updatedat = serializers.DateTimeField(read_only=True)
    category = CategorySerializer(allow_null=True)

    def create(self,validated_data):
        product=Product()
        product.name=validated_data['name']
        product.price=validated_data['price']
        product.description=validated_data['description']
        product.image=validated_data['image']
        product.count=validated_data['count']
        print("helloooooooooooooooooooo================>>>>>>>")
        c=Category.objects.get(id=validated_data['category.id'])
        print("==================>",product.category,c)
        product.category.name = c.name
        product.category.email = c.email
        # product.category.email = validated_data['category.email']
        # product.category.image = validated_data['category.image']
        # product.category.age = validated_data['category.age']
        print("helloooooooooooooooooooo================>>>>>>>")
        # product.save()
        print("helloooooooooooooooooooo================>>>>>>>")
        return product
    
    def update(self,instance,validated_data):
        instance.name=validated_data['name']
        instance.price=validated_data['price']
        instance.description=validated_data['description']
        instance.category=validated_data['category.id']
        instance.save()
        return instance
