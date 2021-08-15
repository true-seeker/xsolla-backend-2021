from django.contrib import admin

from main_app.models import Product, ProductType
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']

admin.site.register(ProductType)
admin.site.register(Product)
