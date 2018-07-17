from django.db import models
from gestion.models import EnumCycle, Eleve, Competence, Classe, Evaluation
from datetime import date
from django.urls import reverse

# Create your models here.
class EnumResultat(models.Model):
	""" enum resultat model """
	literal = models.CharField(max_length=10)
	value = models.IntegerField()

	def __str__(self):
		return self.literal

class Resultat(models.Model):
	""" Resultat model """
	evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
	eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
	competence = models.ForeignKey(Competence, on_delete=models.CASCADE)
	resultat = models.ForeignKey(EnumResultat, on_delete=models.CASCADE)
	created_at = models.DateField(auto_now=False, auto_now_add=True)
	updated_at = models.DateField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.evaluation