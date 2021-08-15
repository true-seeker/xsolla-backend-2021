from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/id/<int:pk>/', views.ProductDetailId.as_view()),
    path('products/sku/<str:stock_keeping_unit>/', views.ProductDetailSKU.as_view()),
    path('product_types/', views.ProductTypeList.as_view()),
    path('product_types/id/<int:pk>/', views.ProductTypeDetailId.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
