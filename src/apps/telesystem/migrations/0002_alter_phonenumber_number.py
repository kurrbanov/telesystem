# Generated by Django 3.2.4 on 2021-06-27 09:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telesystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='number',
            field=models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(12)]),
        ),
    ]