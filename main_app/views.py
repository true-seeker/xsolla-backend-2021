from django.http import HttpResponse


def index(request):
    """View корневой страницы"""
    return HttpResponse("Hello, world!")
