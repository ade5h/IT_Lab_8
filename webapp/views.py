from rest_framework import generics
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Cab
from .serializers import CabSerializer

def get_eta(x1, x2, y1, y2):
	ans = (((x1-x2)*(x1-x2)) + ((y1-y2)*(y1-y2)))/200
	return int(ans)

class CabList(generics.ListCreateAPIView):
	queryset = Cab.objects.all()
	serializer_class = CabSerializer

def getETA(request, pk):
	user_lattitude = int(request.GET['lattitude'])
	user_longitude = int(request.GET['longitude'])

	required_cab = Cab.objects.get(pk=pk)

	fare = int(getattr(required_cab, 'fare'))
	cab_lattitude = int(getattr(required_cab, 'latitude'))
	cab_longitude = int(getattr(required_cab, 'longitude'))

	eta = get_eta(user_lattitude, cab_lattitude, user_longitude, cab_longitude)

	output = {
		'fare': fare,
		'eta': eta
	}

	return JsonResponse(output)