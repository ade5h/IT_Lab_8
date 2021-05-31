from rest_framework import generics
from .models import Location, Seller, Amenity
from .serializers import SellerSerializer, LocationSerializer, AmenitySerializer

class LocationList(generics.ListCreateAPIView):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer

class SellerList(generics.ListCreateAPIView):
	queryset = Seller.objects.all()
	serializer_class = SellerSerializer

class SellerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Seller.objects.all()
	serializer_class = SellerSerializer

class AmenityList(generics.ListCreateAPIView):
	serializer_class = AmenitySerializer

	def get_queryset(self):
		queryset = Amenity.objects.all()

		location = self.request.query_params.get('location')
		if location is not None:
			queryset = queryset.filter(location_id=location)
		
		name = self.request.query_params.get('name')
		if name is not None:
			queryset = queryset.filter(name=name)
		
		return queryset

class AmenityDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Amenity.objects.all()
	serializer_class = AmenitySerializer