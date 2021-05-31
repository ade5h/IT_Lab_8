from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
	path("locations/", views.LocationList.as_view()),
	path("locations/<int:pk>", views.LocationDetail.as_view()),
	path("restaurants/", views.RestaurantList.as_view()),
	path("restaurants/<int:pk>", views.RestaurantDetail.as_view()),
	path("staffs/", views.StaffList.as_view()),
	path("staffs/<int:pk>", views.StaffDetail.as_view())
]