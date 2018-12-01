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



