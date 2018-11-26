from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.sql.datastructures import Join
from django.db.models.signals import post_save

# Create your models here.

class Neighborhood(models.Model):

    '''
	Model that keeps track of neighborhood datas
	'''


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
        ('Nairobi', 'Nairobi'),
    )




    neighborhood_name = models.CharField(max_length=30)
    user = models.ForeignKey(User, related_name="user_neighbor", on_delete=models.CASCADE)
    neighborhood_location = models.CharField(choices=CITY_CHOICES, max_length=200 ,default=0, null=True, blank=True)
    population = models.IntegerField(default=0, null=True, blank=True)
    neighborhood_image = models.ImageField(upload_to='image/' )
    
    

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
    def update_population(cls, id):
        population = cls.objects.filter(id=id).update(id=id).count()
        return population



class Business(models.Model):

    '''
	Model that keeps track of business datas
	'''


    business_name = models.CharField(max_length=30, null=True)
    business_location = models.CharField(max_length=20)
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



class Profile(models.Model):

    '''
	Model that keeps track of profile datas
	'''


    class Meta:
        db_table = 'profile'

    bio = models.TextField(max_length=200, null=True, blank=True, default="bio")
    profile_pic = models.ImageField(upload_to='picture/', null=True, blank=True, default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="prof")
    email= models.TextField(max_length=200, null=True, blank=True, default=0)
    neighborhood_id = models.ForeignKey(Neighborhood, on_delete=models.CASCADE,related_name="neighborhood",null=True,blank=True)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_users(cls, search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term)
        return profiles

    @property
    def image_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url

    def __str__(self):
        return self.user.username  

class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name  



class Image(models.Model):

    '''
	Model that keeps track of image datas
	'''

    image = models.ImageField(upload_to='picture/', )
    name = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="images")
    description = models.TextField()
    location = models.ForeignKey(Location, null=True)
    likes = models.IntegerField(default=0)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    @classmethod
    def delete_image_by_id(cls, id):
        pictures = cls.objects.filter(pk=id)
        pictures.delete()

    @classmethod
    def get_image_by_id(cls, id):
        pictures = cls.objects.get(pk=id)
        return pictures

    @classmethod
    def filter_by_location(cls, location):
        pictures = cls.objects.filter(location=location)
        return pictures

    @classmethod
    def search_image(cls, search_term):
        pictures = cls.objects.filter(name__icontains=search_term)
        return pictures

    @classmethod
    def update_image(cls, id):
        pictures = cls.objects.filter(id=id).update(id=id)
        return pictures   


class Join(models.Model):
	'''
	Model that keeps track of what user has joined what neighborhood
	'''
	user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name="neighborhooduser",null=True,blank=True)
	neighborhood_id = models.ForeignKey(Neighborhood, on_delete=models.CASCADE,related_name="neighborhoodjoined",null=True,blank=True)

	def __str__(self):
		return self.user_id            
