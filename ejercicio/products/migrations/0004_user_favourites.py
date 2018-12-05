# Generated by Django 2.1.4 on 2018-12-05 18:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_user_favourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favourites',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, default=[], size=None),
        ),
    ]