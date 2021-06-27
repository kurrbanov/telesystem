from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Неверный логин или пароль.')

    return render(request, 'accounts/login.html', {})


def logout_page(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html', {})


@login_required(login_url='login')
def find(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']


        return render(request, 'subscriber_information.html', {})

    return render(request, 'subscriber_information.html', {})

