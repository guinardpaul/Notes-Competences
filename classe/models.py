from django.db import models

# Create your models here.
class Classe(models.Model):
	""" Classe models """
	nom = models.CharField(max_length=200)
	cycle = models.CharField(max_length=200)

	def __str__(self):
		return self.nom