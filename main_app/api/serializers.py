from rest_framework import serializers

from main_app.models import Product, ProductType


class ProductTypeSerializer(serializers.ModelSerializer):
    """Сериалазейр класса ProductType"""

    class Meta:
        model = ProductType
        fields = ['id', 'title']

    def update(self, instance, validated_data):
        """Метод для обновления информации о типе продукта с помощью метода PUT"""
        instance.title = validated_data.get('title', instance.title)
        instance.save()

        return instance


class ProductSerializer(serializers.ModelSerializer):
    """Сериалазейр класса Product"""

    class Meta:
        model = Product
        fields = ['id', 'stock_keeping_unit', 'title', 'product_type', 'price']

    def update(self, instance, validated_data):
        """Метод для обновления информации о продукте с помощью метода PUT"""
        instance.stock_keeping_unit = validated_data.get('stock_keeping_unit', instance.stock_keeping_unit)
        instance.title = validated_data.get('title', instance.title)
        instance.product_type = validated_data.get('product_type', instance.product_type)
        instance.price = validated_data.get('price', instance.price)
        instance.save()

        return instance
