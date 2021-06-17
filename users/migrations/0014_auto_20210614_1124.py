# Generated by Django 3.1.7 on 2021-06-14 08:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20210613_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 14, 8, 54, 20, 391807, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='activation',
            name='token',
            field=models.CharField(default='e16108ba32ce9a0c9ac71abc09b0147399079399b75816bbccbaac717e82519e', max_length=64),
        ),
    ]