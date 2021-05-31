from django.db import models

class Location(models.Model):
	name = models.CharField(max_length=50)
	pincode = models.CharField(max_length=50)
	area = models.IntegerField()
	
	def __str__(self):
		return self.name

class Restaurant(models.Model):
	name = models.CharField(max_length=50)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	cuisine = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Staff(models.Model):
	name = models.CharField(max_length=50)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	years_of_experience = models.IntegerField()

	def __str__(self):
		return self.name