from django.shortcuts import render

from main_app.models import Product


def index(request):
    """View корневой страницы"""

    products = Product.objects.all()
    return render(request, 'index.html', context={'products': products})
