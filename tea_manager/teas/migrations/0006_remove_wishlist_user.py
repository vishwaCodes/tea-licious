# Generated by Django 3.1.7 on 2021-03-04 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teas', '0005_auto_20210304_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='user',
        ),
    ]
