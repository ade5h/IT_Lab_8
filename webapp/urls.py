from django.urls import path

from . import views

urlpatterns = [
	path("locations/", views.LocationList.as_view()),
	path("locations/<int:pk>", views.LocationDetail.as_view()),
	path("sellers/", views.SellerList.as_view()),
	path("sellers/<int:pk>", views.SellerDetail.as_view()),
	path("amenities/", views.AmenityList.as_view()),
	path("amenities/<int:pk>", views.AmenityDetail.as_view())
]