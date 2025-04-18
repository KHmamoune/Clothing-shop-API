from rest_framework import serializers
from .models import Product, Promotion, Size, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PromotionSerializer(serializers.ModelSerializer):
    product = ProductSerializer(source='id_product', read_only=True)

    class Meta:
        model = Promotion
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'
