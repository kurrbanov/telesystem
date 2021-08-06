# Generated by Django 3.2.4 on 2021-06-27 09:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('patronymic', models.CharField(max_length=255)),
                ('passport', models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('cities', models.CharField(choices=[('1', 'Екатеринбург'), ('2', 'Елабуга'), ('3', 'Зеленодольск'), ('4', 'Иннополис'), ('5', 'Казань'), ('6', 'Краснодар'), ('7', 'Москва'), ('8', 'Санкт-Петербург'), ('9', 'Сочи')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11)])),
                ('rate', models.CharField(blank=True, choices=[('1', 'Ультра'), ('2', 'Smart'), ('3', 'Безлимитище'), ('4', 'Тарифище')], max_length=2)),
                ('balance', models.FloatField()),
                ('minutes', models.IntegerField()),
                ('internet', models.FloatField()),
                ('sms', models.IntegerField()),
                ('date_payment', models.DateField()),
                ('subscriber', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='telesystem.subscriber')),
            ],
        ),
    ]