from django.db import models

class Cab(models.Model):
	name = models.CharField(max_length=50)
	rating = models.IntegerField()
	latitude = models.DecimalField(max_digits=7,decimal_places=4)
	longitude = models.DecimalField(max_digits=7,decimal_places=4)
	fare = models.IntegerField()
	
	def __str__(self):
		return self.name