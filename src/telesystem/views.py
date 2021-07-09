from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from .forms import *
from datetime import date


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
    if request.method == 'POST':
        try:
            phone_number = PhoneNumber.objects.get(number=request.POST['phone_number'])
        except ObjectDoesNotExist:
            return render(request, 'subscriber_information.html', {'found': False})

        return render(request, 'subscriber_information.html', {
            'subscriber': phone_number.subscriber,
            'phone_info': phone_number,
            'found': True
        })

    return render(request, 'subscriber_information.html', {})


@login_required(login_url='login')
def add(request):
    rate_property = {
        'Ультра': {
            'balance': 800,
            'internet': 50,
            'minutes': 1500,
            'sms': 1500
        },
        'Smart': {
            'balance': 500,
            'internet': 30,
            'minutes': 500,
            'sms': 500
        },
        'Безлимитище': {
            'balance': 450,
            'internet': 25,
            'minutes': 400,
            'sms': 400
        },
        'Тарифище': {
            'balance': 400,
            'internet': 25,
            'minutes': 600,
            'sms': 600
        }
    }
    if request.method == 'POST':
        form_subscriber = SubscriberForm(request.POST)
        form_phone = PhoneNumberForm(request.POST)
        if form_subscriber.is_valid() and form_phone.is_valid():
            subscriber = form_subscriber.save()
            phone = form_phone.save(commit=False)
            phone.subscriber = subscriber
            phone.balance = rate_property[phone.rate]['balance']
            phone.minutes = rate_property[phone.rate]['minutes']
            phone.internet = rate_property[phone.rate]['internet']
            phone.sms = rate_property[phone.rate]['sms']
            custom_date = date.today()
            phone.date_payment = date(custom_date.year, custom_date.month + 1, custom_date.day)
            phone.save()
            return redirect('index')
        else:
            messages.error(request, 'Форма заполнена неверно')

    return render(request, 'sub_add.html')


@login_required(login_url='login')
def add_number(request, pk):
    rate_property = {
        'Ультра': {
            'balance': 800,
            'internet': 50,
            'minutes': 1500,
            'sms': 1500
        },
        'Smart': {
            'balance': 500,
            'internet': 30,
            'minutes': 500,
            'sms': 500
        },
        'Безлимитище': {
            'balance': 450,
            'internet': 25,
            'minutes': 400,
            'sms': 400
        },
        'Тарифище': {
            'balance': 400,
            'internet': 25,
            'minutes': 600,
            'sms': 600
        }
    }
    if request.method == "POST":
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            subscriber = Subscriber.objects.get(id=pk)
            phone = form.save(commit=False)
            phone.subscriber = subscriber
            phone.balance = rate_property[phone.rate]['balance']
            phone.minutes = rate_property[phone.rate]['minutes']
            phone.internet = rate_property[phone.rate]['internet']
            phone.sms = rate_property[phone.rate]['sms']
            custom_date = date.today()
            phone.date_payment = date(custom_date.year, custom_date.month + 1, custom_date.day)
            phone.save()
            return redirect('index')
        else:
            messages.error(request, 'Номер уже занят.')

    return render(request, 'number_add.html')


@login_required(login_url='login')
def sub_change(request, pk):
    sub = Subscriber.objects.get(id=pk)
    form = SubscriberForm(instance=sub)
    if request.method == 'POST':
        form = SubscriberForm(request.POST, instance=sub)
        if form.is_valid():
            form.save()
            redirect('index')
        else:
            messages.error(request, 'Форма заполнена неверно.')

    return render(request, 'sub_change.html', {'form': form})


@login_required(login_url='login')
def sub_delete(request, pk):
    sub = Subscriber.objects.get(id=pk)
    if request.method == 'POST':
        sub.delete()
        return redirect('index')

    return render(request, 'sub_delete.html', {'subscriber': sub})
