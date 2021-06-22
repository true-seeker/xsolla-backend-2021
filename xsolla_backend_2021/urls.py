"""
xsolla_backend_2021 URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/', include('main_app.api.urls')),
]
