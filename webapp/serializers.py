from rest_framework import serializers
from .models import Location, Seller, Amenity

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = "__all__"

class SellerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Seller
		fields = "__all__"

class AmenitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Amenity
		fields = "__all__"