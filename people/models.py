from django.db import models

class Person(models.Model):
	image = models.ImageField(upload_to='images/')
	name = models.CharField(max_length=50)
	title = models.CharField(max_length=50)
	desc = models.CharField(max_length=200)
