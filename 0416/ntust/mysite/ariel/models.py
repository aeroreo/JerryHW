from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=15)
	address = models.CharField(max_length=50, blank=True)
	is_boy = models.BooleanField(default = False)


	def __str__(self):
			return self.name	