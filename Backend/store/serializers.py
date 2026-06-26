from rest_framework import serializers
from .models import Categort, Product,Cart,CartItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categort
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Nested serializer to include category details

    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    product_name=serializers.CharField(source="product.name",read_only=True)
    product_price=serializers.DecimalField(source="product.price",read_only=True,decimal_places=2,max_digits=10)
    product_image=serializers.ImageField(source="product.image",read_only=True)

    class Meta:
        model=CartItem
        fields="__all__"

class CadSerializer(serializers.ModelSerializer):
    item=CartItemSerializer(many=True,read_only=True)
    total=serializers.ReadOnlyField()

    class Meta:
        model=Cart
        fields="__all__"

