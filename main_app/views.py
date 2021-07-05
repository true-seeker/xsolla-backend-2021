from django.shortcuts import redirect


def index(request):
    """View корневой страницы"""

    return redirect('https://github.com/true-seeker/xsolla-backend-2021')
