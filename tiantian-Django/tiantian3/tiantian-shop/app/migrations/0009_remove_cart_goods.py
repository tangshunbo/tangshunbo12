# Generated by Django 2.1 on 2018-08-21 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='goods',
        ),
    ]
