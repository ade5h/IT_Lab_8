from django.contrib import admin

from .models import Location, Seller, Amenity

admin.site.register(Location)
admin.site.register(Seller)
admin.site.register(Amenity)