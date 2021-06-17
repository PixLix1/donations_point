# Generated by Django 3.1.7 on 2021-06-14 09:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20210614_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 14, 10, 5, 10, 112810, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='activation',
            name='token',
            field=models.CharField(default='5615eb6e0e4e3e401deddcf306bea32e2519bf9d9e430415ed953e147a565bc1', max_length=64),
        ),
    ]