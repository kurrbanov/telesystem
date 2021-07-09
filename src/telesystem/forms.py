from django.forms import ModelForm

from .models import *


class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SubscriberForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class PhoneNumberForm(ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['number', 'rate']
