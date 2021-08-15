from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from main_app.models import Product


def index(request):
    """View корневой страницы"""
    return render(request, 'index.html')


def signup(request):
    """view авторизации"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # Проверка валидности формы
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
