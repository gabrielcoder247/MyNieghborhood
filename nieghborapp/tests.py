from __future__ import unicode_literals
from django.test import TestCase
from .models import *
from django.contrib.auth.models import User


# Create your tests here.


class NeighborhoodTestClass(TestCase):

    def setUp(self):
        self.neighborhood=Neighborhood(neighborhood_name='nairobi', 
                            neighborhood_location='kenya',
                            population='100',
                          )

    def test_instance(self):
        self.assertTrue(isinstance(self.neighborhood,Neighborhood))                        
    # test methods
    def test_save_method(self):
        self.neighborhood.save()
        neighborhood_obj = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood_obj)>0)  

    def test_delete_neighborhood_by_id(self):
        neighborhood_delete = Neighborhood.objects.filter(id=1)
        neighborhood_delete.delete()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood)==0)

    def  test_get_neighborhood_by_id(self):
        self.neighborhood.save()
        neighborhood = Neighborhood.objects.get(id=1)
        self.assertTrue(neighborhood.neighborhood_name,'langata')

    def test_search_neighborhood(self):
        self.neighborhood.save()
        neighborhood = Neighborhood.objects.filter(neighborhood_name__icontains ='nairobi')
        self.assertTrue(len(neighborhood)>0)

class BusinessTestclass(TestCase):
    # test methods
    def setUp(self):
        self.business = Business(business_name='edu enterprise',
                                business_location='nairobi',
                                business_email_address='edu@gmail.com',
                                ) 

    def test_instance(self):
            self.assertTrue(isinstance(self.business,Business)) 

    def test_save_method(self):
        self.business.save()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)


    def delete_business_by_id(self):
        business_delete = Business.objects.filter(id=1)
        business_delete.delete()
        business = Business.objects.all()
        self.assertTrue(len(business)==0)

    def test_search_business(self):
        self.business.save()
        business = Business.objects.filter(business_name__icontains ='edu enterprise')
        self.assertTrue(len(business)>0)
    



