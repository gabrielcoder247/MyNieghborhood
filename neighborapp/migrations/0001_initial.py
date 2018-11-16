# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-16 10:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=30, null=True)),
                ('business_email_address', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighborhood_name', models.CharField(max_length=30)),
                ('neighborhood_location', models.CharField(blank=True, choices=[('London', 'London'), ('Moscow', 'Moscow'), ('St. peterburge', 'St. peterburge'), ('Nizhny Novgorod', 'Nizhny Novgorod'), ('New york', 'New york'), ('Abuja', 'Abuja'), ('Lagos', 'Lagos'), ('Perm', 'Perm'), ('Kazan', 'Kazan'), ('Sochi', 'Sochi')], default=0, max_length=200, null=True)),
                ('ocuppants_count', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='neighborhood_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhood_class', to='neighborapp.Neighborhood'),
        ),
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_class', to=settings.AUTH_USER_MODEL),
        ),
    ]