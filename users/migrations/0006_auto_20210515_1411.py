# Generated by Django 3.1.7 on 2021-05-15 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210515_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default=None, null=True, upload_to='profiles'),
        ),
    ]
