# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-01 08:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nieghborapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighborhood',
            name='business_id',
        ),
    ]