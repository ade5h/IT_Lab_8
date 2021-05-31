from rest_framework import generics
from .models import Restaurant, Location, Staff
from .serializers import RestaurantSerializer, LocationSerializer, StaffSerializer

class LocationList(generics.ListCreateAPIView):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer

class RestaurantList(generics.ListCreateAPIView):
	serializer_class = RestaurantSerializer

	def get_queryset(self):
		queryset = Restaurant.objects.all()
		location = self.request.query_params.get('location')
		if location is not None:
			queryset = queryset.filter(location_id=location)
		
		name = self.request.query_params.get('name')
		if name is not None:
			queryset = queryset.filter(name=name)

		cuisine = self.request.query_params.get('cuisine')
		if cuisine is not None:
			queryset = queryset.filter(cuisine=cuisine)
		
		return queryset

class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantSerializer

class StaffList(generics.ListCreateAPIView):
	queryset = Staff.objects.all()
	serializer_class = StaffSerializer

class StaffDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Staff.objects.all()
	serializer_class = StaffSerializer