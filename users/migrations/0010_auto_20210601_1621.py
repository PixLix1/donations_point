# Generated by Django 3.1.7 on 2021-06-01 13:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_activation'),
    ]

    operations = [
        migrations.AddField(
            model_name='activation',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 13, 51, 51, 695997, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='activation',
            name='token',
            field=models.CharField(default='bcafe5e489f96dcf2aa2ddb78f4fcdf978d4b99e1497621a20cef6d18aa5f307', max_length=64),
        ),
    ]