from rest_framework import generics

from main_app.models import Product
from . import serializers
from .paginators import ItemSetPagination


class ProductList(generics.ListCreateAPIView):
    """Обработка get api/products"""
    serializer_class = serializers.ProductSerializer
    pagination_class = ItemSetPagination

    def get_queryset(self):
        queryset = Product.objects.all()
        product_type = self.request.query_params.get('product_type')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if product_type:
            queryset = queryset.filter(product_type_id=product_type)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset

    def perform_create(self, serializer):
        """Обработка post запросов"""
        serializer.save()


class ProductDetailId(generics.RetrieveUpdateDestroyAPIView):
    """Обработка get, update, delete api/products/id/<id>"""
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDetailSKU(generics.RetrieveUpdateDestroyAPIView):
    """Обработка get, update, delete api/products/sku/<stock_keeping_unit>"""
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    lookup_field = 'stock_keeping_unit'
