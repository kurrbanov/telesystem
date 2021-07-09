from django.forms import ModelForm

from .models import *


class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'


class PhoneNumberForm(ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['number', 'rate']
