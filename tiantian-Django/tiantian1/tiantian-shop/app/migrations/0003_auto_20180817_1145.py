# Generated by Django 2.1 on 2018-08-17 03:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180815_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=6, message='请输入6到20位用户名')], verbose_name='用户名'),
        ),
    ]
