from rest_framework import serializers

from product.models import CategoryModel, ProductModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["id", "name", "description", "created_at", "updated_at"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = [
            "category",
            "name",
            "description",
            "price",
            "created_at",
            "updated_at",
        ]
