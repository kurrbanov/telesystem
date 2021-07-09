from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from .models import *


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
    return render(request, 'index.html')


@login_required(login_url='login')
def find(request):
    CITIES = [
        ('Екатеринбург', 'Екатеринбург'),
        ('Елабуга', 'Елабуга'),
        ('Зеленодольск', 'Зеленодольск'),
        ('Иннополис', 'Иннополис'),
        ('Казань', 'Казань'),
        ('Краснодар', 'Краснодар'),
        ('Москва', 'Москва'),
        ('Санкт-Петербург', 'Санкт-Петербург'),
        ('Сочи', 'Сочи')
    ]
    
    RATES = [
        ('Ультра', 'Ультра'),
        ('Smart', 'Smart'),
        ('Безлимитище', 'Безлимитище'),
        ('Тарифище', 'Тарифище')
    ]
    
    if request.method == 'POST':
        try:
            phone_number = PhoneNumber.objects.get(number=request.POST['phone_number'])
        except ObjectDoesNotExist:
            print('yes')
            return render(request, 'subscriber_information.html', {'found': False})

        city = ''
        for c in CITIES:
            if c[0] == phone_number.subscriber.cities:
                city = c[1]
        rate = ''
        for r in RATES:
            if r[0] == phone_number.rate:
                rate = r[1]

        return render(request, 'subscriber_information.html', {
            'subscriber': phone_number.subscriber,
            'phone_info': phone_number,
            'city': city,
            'rate': rate,
            'found': True
        })

    return render(request, 'subscriber_information.html', {})

