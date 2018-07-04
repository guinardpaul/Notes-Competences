from django.db import models
from django.urls import reverse

# Create your models here.
CYCLE = (
		('Cycle 3', 'Cycle 3'),
		('Cycle 4', 'Cycle 4'),
		)

class EnumCycle(models.Model):
	""" enum cycle model """
	literal = models.CharField(max_length=10)
	value = models.IntegerField()

	def __str__(self):
		return self.literal

class Classe(models.Model):
	""" Classe model. """
	nom = models.CharField(max_length=5, unique=True)
	cycle = models.ForeignKey(EnumCycle, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('gestion:classe_detail', kwargs={ 'pk': self.pk })

	def __str__(self):
		return self.nom

class Eleve(models.Model):
	""" Eleve model. """
	nom = models.CharField(max_length=200)
	prenom = models.CharField(max_length=200)
	classe = models.ForeignKey(Classe, on_delete=models.CASCADE, default=-1, null=True)

	def get_absolute_url(self):
		return reverse('gestion:eleve_detail', kwargs={ 'pk': self.pk })

	def __str__(self):
		return self.nom + ' ' + self.prenom

class Domaine(models.Model):
	""" Domaine model. """
	ref = models.CharField(max_length=10)
	description = models.TextField()
	cycle = models.ForeignKey(EnumCycle, on_delete=models.CASCADE)
	sous_domaine = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, default=None, null=True)

	class meta:
		unique_together = ('ref', 'cycle')

	def get_absolute_url(self):
		if self.sous_domaine != None:
			return reverse('gestion:domaine_detail', kwargs={ 'pk': self.sous_domaine.id })
		else:
			return reverse('gestion:domaine_detail', kwargs={ 'pk': self.pk })

	def __str__(self):
		return self.ref + " - " + self.description

class Competence(models.Model):
	""" Competence model. """
	ref = models.CharField(max_length=10)
	description = models.TextField()
	cycle = models.ForeignKey(EnumCycle, on_delete=models.CASCADE)
	domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)

	class meta:
		unique_together = ('ref', 'cycle')

	def get_absolute_url(self):
		redirect_domaine = None
		domaine = Domaine.objects.get(pk=self.domaine.id)

		if domaine.sous_domaine != None:
			redirect_domaine = Domaine.objects.get(pk=domaine.sous_domaine.id)
		else:
			redirect_domaine = domaine
		
		return reverse('gestion:domaine_detail', kwargs={ 'pk': redirect_domaine.id })
	
	def __str__(self):
		return self.ref
