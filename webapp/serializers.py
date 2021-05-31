from rest_framework import serializers
from .models import Restaurant, Location, Staff

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = "__all__"

class RestaurantSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = "__all__"

class StaffSerializer(serializers.ModelSerializer):
	class Meta:
		model = Staff
		fields = "__all__"