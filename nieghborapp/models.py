from django.db import models

# Create your models here.

class Neighborhood(models.Model):
    CITY_CHOICES = (

        ('London', 'London'),
        ('Moscow', 'Moscow'),
        ('St. peterburge', 'St. peterburge'),
        ('Nizhny Novgorod', 'Nizhny Novgorod'),
        ('New york', 'New york'),
        ('Abuja', 'Abuja'),
        ('Lagos', 'Lagos'),
        ('Perm', 'Perm'),
        ('Kazan', 'Kazan'),
        ('Sochi', 'Sochi'),
    )



