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




    neighborhood_name = models.CharField(max_length=30)
    neighborhood_location = models.CharField(choices=CITY_CHOICES, max_length=200 ,default=0, null=True, blank=True)
    ocuppants_count = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.neighborhood_name

    def save_neighborhood(self):
        self.save()

    @classmethod
    def delete_neighborhood_by_id(cls, id):
        neighborhoods = cls.objects.filter(pk=id)
        neighborhoods.delete()

    @classmethod
    def get_neighborhood_by_id(cls, id):
        neighborhoods = cls.objects.get(pk=id)
        return neighborhoods

    @classmethod
    def filter_by_location(cls, location):
        neighborhoods = cls.objects.filter(location=location)
        return neighborhoods

    @classmethod
    def search_neighborhood(cls, search_term):
        neighborhoods = cls.objects.filter(neighborhood_name__icontains=search_term)
        return neighborhoods

    @classmethod
    def update_neighborhood(cls, id):
        neighborhoods = cls.objects.filter(id=id).update(id=id)
        return neighborhoods

    @classmethod
    def update_occupants(cls, id):
        occupants = cls.objects.filter(id=id).update(id=id)
        return occupants



class Business(models.Model):
    business_name = models.CharField(max_length=30, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user_class")
    neighborhood_id = models.ForeignKey(Neighborhood, on_delete=models.CASCADE,related_name="neighbourhood_class",null=True,blank=True)
    business_email_address = models.CharField(max_length=200, null = True)

    def __str__(self):
        return self.business_name


    def save_business(self):
        self.save()

    @classmethod
    def delete_business_by_id(cls, id):
        businesses = cls.objects.filter(pk=id)
        businesses.delete()

    @classmethod
    def find_business_by_id(cls, id):
        business = cls.objects.get(pk=id)
        return business

    @classmethod
    def filter_by_location(cls, location):
        businesses = cls.objects.filter(location=location)
        return businesses

    @classmethod
    def search_business(cls, search_term):
        business = cls.objects.filter(business_name__icontains=search_term)
        return business

    @classmethod
    def update_business(cls, id):
        business = cls.objects.filter(id=id).update(id=id)
        return business
