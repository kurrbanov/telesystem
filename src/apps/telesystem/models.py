from django.db import models
from django.core.validators import MinLengthValidator


class Subscriber(models.Model):
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

    name = models.CharField(max_length=255, blank=False)  # имя
    surname = models.CharField(max_length=255, blank=False)  # фамилия
    patronymic = models.CharField(max_length=255, blank=False)  # отчество
    passport = models.CharField(max_length=10, blank=False, unique=True, validators=[MinLengthValidator(10)])  # паспорт
    cities = models.CharField(choices=CITIES, max_length=30, blank=False)  # город

    def __str__(self):
        return f"{self.name} {self.surname} {self.patronymic}"


class PhoneNumber(models.Model):
    RATES = [
        ('Ультра', 'Ультра'),
        ('Smart', 'Smart'),
        ('Безлимитище', 'Безлимитище'),
        ('Тарифище', 'Тарифище')
    ]

    number = models.CharField(max_length=12, validators=[MinLengthValidator(12)], blank=False,
                              unique=True)  # номер телефона
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE, blank=False)  # Владелец номера
    rate = models.CharField(choices=RATES, max_length=30, blank=False)  # тариф
    balance = models.FloatField(blank=False)  # баланс
    minutes = models.IntegerField(blank=False)  # остаток минут
    internet = models.FloatField(blank=False)  # остаток интерента
    sms = models.IntegerField(blank=False)  # отстаток смс
    date_payment = models.DateField(blank=False)  # дата списания денег с тарифа

    def __str__(self):
        return f"{self.number}"
