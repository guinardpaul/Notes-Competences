from django.db import models

# Create your models here.
CYCLE = (
		('Cycle 3', 'Cycle 3'),
		('Cycle 4', 'Cycle 4'),
		)

class Classe(models.Model):
	""" Classe model. """
	nom = models.CharField(max_length=5, unique=True)
	cycle = models.CharField(max_length=7, choices=CYCLE)

	def __str__(self):
		return self.nom

class Eleve(models.Model):
	""" Eleve model. """
	nom = models.CharField(max_length=200)
	prenom = models.CharField(max_length=200)
	classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

	def __str__(self):
		return self.nom + ' ' + self.prenom

class Domaine(models.Model):
	""" Domaine model. """
	ref = models.CharField(max_length=10, unique=True)
	description = models.CharField(max_length=200)
	cycle = models.CharField(max_length=7, choices=CYCLE)

	def __str__(self):
		return self.ref

class Competence(models.Model):
	""" Competence model. """
	ref = models.CharField(max_length=10, unique=True)
	description = models.CharField(max_length=200)
	cycle = models.CharField(max_length=7, choices=CYCLE)
	domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)

	def __str__(self):
		return self.ref
