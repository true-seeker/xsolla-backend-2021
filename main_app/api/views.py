from rest_framework import generics
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from main_app.models import Product, ProductType
from . import serializers
from .exceptions import ProductTypeException, MinPriceException, MaxPriceException
from .paginators import ProductsPagination


class ProductListGet(generics.ListAPIView):
    """Обработка get api/products/get"""
    serializer_class = serializers.ProductSerializer
    pagination_class = ProductsPagination

    # Указание типа авторизации
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Фильтр возвращаемых данных по GET параметрам"""
        queryset = Product.objects.all()
        product_type = self.request.query_params.get('product_type')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if product_type:
            try:
                int(product_type)
            except ValueError:
                raise ProductTypeException
            queryset = queryset.filter(product_type_id=product_type)

        if min_price:
            try:
                int(min_price)
            except ValueError:
                raise MinPriceException
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            try:
                float(max_price)
            except ValueError:
                raise MaxPriceException
            queryset = queryset.filter(price__lte=max_price)

        return queryset


class ProductList(generics.CreateAPIView):
    """Обработка post api/products"""

    serializer_class = serializers.ProductSerializer
    pagination_class = ProductsPagination
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class ProductDetailId(generics.UpdateAPIView, generics.DestroyAPIView):
    """Обработка update, delete api/products/id/<id>"""
    # Кастомная проверка разрешений изменение и чтение
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDetailIdGet(generics.RetrieveAPIView):
    """Обработка get api/get/products/id/<id>"""
    # Кастомная проверка разрешений изменение и чтение
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDetailSKU(generics.UpdateAPIView, generics.DestroyAPIView):
    """Обработка update, delete api/products/sku/<stock_keeping_unit>"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    lookup_field = 'stock_keeping_unit'


class ProductDetailSKUGet(generics.RetrieveAPIView):
    """Обработка get api/products/get/sku/<stock_keeping_unit>"""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    lookup_field = 'stock_keeping_unit'


class ProductTypeListGet(generics.ListAPIView):
    """Обработка get api/product_types/get/"""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ProductType.objects.all()
    serializer_class = serializers.ProductTypeSerializer


class ProductTypeList(generics.CreateAPIView):
    """Обработка post api/product_types/"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ProductType.objects.all()
    serializer_class = serializers.ProductTypeSerializer


class ProductTypeDetailIdGet(generics.RetrieveAPIView):
    """Обработка get api/product_types/get/id/<id>"""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ProductTypeSerializer
    queryset = ProductType.objects.all()


class ProductTypeDetailId(generics.UpdateAPIView, generics.DestroyAPIView):
    """Обработка update, delete api/product_types/id/<id>"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ProductTypeSerializer
    queryset = ProductType.objects.all()
