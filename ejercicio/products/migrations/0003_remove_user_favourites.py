# Generated by Django 2.1.4 on 2018-12-05 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_user_favourites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favourites',
        ),
    ]
