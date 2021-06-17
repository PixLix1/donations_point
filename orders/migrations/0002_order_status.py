# Generated by Django 3.1.7 on 2021-06-15 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('1', 'Open'), ('2', 'Approved'), ('3', 'Rejected'), ('4', 'Shipment'), ('5', 'Closed')], default='1', max_length=2),
        ),
    ]
