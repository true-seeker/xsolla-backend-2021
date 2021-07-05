from django.shortcuts import redirect

from main_app.models import Product


def index(request):
    """View корневой страницы"""
    return redirect('https://github.com/true-seeker/xsolla-backend-2021')
