from django.db import models

class Location(models.Model):
	name = models.CharField(max_length=50)
	pincode = models.CharField(max_length=50)
	area = models.IntegerField()
	
	def __str__(self):
		return self.name

class Seller(models.Model):
	name = models.CharField(max_length=50)
	rating = models.IntegerField()

	def __str__(self):
		return self.name

class Amenity(models.Model):
	name = models.CharField(max_length=50)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
	quantity = models.IntegerField()

	def __str__(self):
		return self.name