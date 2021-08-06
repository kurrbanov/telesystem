from django.contrib import admin

from .models import *


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'patronymic', 'passport', 'cities')


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'rate', 'get_subscriber_name', 'get_subscriber_patronymic', 'balance')

    @staticmethod
    def get_subscriber_name(obj):
        return obj.subscriber.name

    @staticmethod
    def get_subscriber_patronymic(obj):
        return obj.subscriber.patronymic

    get_subscriber_name.short_description = 'Subscriber'
    get_subscriber_name.admin_order_field = 'subscriber__name'

    get_subscriber_patronymic.short_description = 'Subscriber'
    get_subscriber_patronymic.admin_order_field = 'subscriber__patronymic'
