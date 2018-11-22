from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Neighborhood,NeighborhoodAdmin)
admin.site.register(Business,BusinessAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(Image,ImageAdmin)
