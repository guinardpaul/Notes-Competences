from django.db import models
from gestion.models import EnumCycle, Eleve, Competence
from datetime import date

# Create your models here.
class EnumResultat(models.Model):
	""" enum resultat model """
	literal = models.CharField(max_length=10)
	value = models.IntegerField()

	def __str__(self):
		return self.literal

class EnumTrimestre(models.Model):
	""" enum trimestre model """
	literal = models.CharField(max_length=10)
	value = models.IntegerField()

	def __str__(self):
		return self.literal

class Evaluation(models.Model):
	""" Evaluation model """
	description = models.CharField(max_length=200)
	created_at = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
	trimestre = models.ForeignKey(EnumTrimestre, on_delete=models.CASCADE)
	cycle = models.ForeignKey(EnumCycle, on_delete=models.CASCADE)

	def __str__(self):
		return self.description

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