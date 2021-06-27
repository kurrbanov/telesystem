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
    return render(request, 'index.html', {})


@login_required(login_url='login')
def find(request):
    CITIES = [
        ('1', 'Екатеринбург'),
        ('2', 'Елабуга'),
        ('3', 'Зеленодольск'),
        ('4', 'Иннополис'),
        ('5', 'Казань'),
        ('6', 'Краснодар'),
        ('7', 'Москва'),
        ('8', 'Санкт-Петербург'),
        ('9', 'Сочи')
    ]
    
    RATES = [
        ('1', 'Ультра'),
        ('2', 'Smart'),
        ('3', 'Безлимитище'),
        ('4', 'Тарифище')
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

