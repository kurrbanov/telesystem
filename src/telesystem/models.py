from django.db import models


class Subscriber(models.Model):
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

    name = models.CharField(max_length=255, blank=False)  # имя
    surname = models.CharField(max_length=255, blank=False)  # фамилия
    patronymic = models.CharField(max_length=255, blank=False)  # отчество
    phone_number = models.CharField(max_length=11, blank=False)  # номер телефона
    cities = models.CharField(choices=CITIES, max_length=3, blank=False)  # город
    rate = models.CharField(choices=RATES, max_length=2, blank=False)  # тариф
    balance = models.FloatField(blank=False)  # баланс
    minutes = models.IntegerField(blank=False)  # остаток минут
    internet = models.FloatField(blank=False)  # остаток интерента
    sms = models.IntegerField(blank=False)  # отстаток смс
    last_date_payment = models.DateField()  # последний день оплаты тарифа
