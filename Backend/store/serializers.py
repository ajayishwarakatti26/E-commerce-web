from rest_framework import serializers
from .models import Categort, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categort
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Nested serializer to include category details

    class Meta:
        model = Product
        fields = '__all__'