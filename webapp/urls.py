from django.urls import path

from . import views

urlpatterns = [
	path("cabs/", views.CabList.as_view()),
	path("cabs/<int:pk>", views.getETA)
]