from django.contrib import admin

from main_app.models import Product, ProductType

admin.site.register(ProductType)
admin.site.register(Product)
