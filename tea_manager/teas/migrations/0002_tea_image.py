# Generated by Django 3.1.7 on 2021-03-02 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tea',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]