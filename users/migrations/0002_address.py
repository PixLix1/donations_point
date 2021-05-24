# Generated by Django 3.1.7 on 2021-05-06 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial')
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=255)),
                ('county', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('comments', models.CharField(max_length=255, null=True)),
                ('type', models.IntegerField(choices=[(1, 'Shipping'), (2, 'Billing')], default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]