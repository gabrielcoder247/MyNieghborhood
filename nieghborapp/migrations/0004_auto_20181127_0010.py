# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-26 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nieghborapp', '0003_auto_20181126_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='neighborhood_image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
