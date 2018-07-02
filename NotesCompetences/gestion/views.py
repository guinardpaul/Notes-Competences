from django.http import Http404
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Classe, Eleve, Domaine, Competence
from itertools import chain
from . import forms
# Create your views here.
# CLASSE Views
@method_decorator(login_required, name='dispatch')
class ClasseListView(generic.ListView):
	""" Affiche la liste des classes """
	template_name = 'gestion/classe_list.html'
	context_object_name = 'classe_list'

	def get_queryset(self):
		return Classe.objects.all().order_by('cycle', 'nom')

@method_decorator(login_required, name='dispatch')
class ClasseDetail(generic.DetailView):
	""" Detail d'une classe avec les eleves """
	model = Classe
	template_name = 'gestion/classe_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		try:
			eleves = Eleve.objects.filter(classe=context['classe'].id)
		except Eleve.DoesNotExist:
			raise Http404("L'object auquel vous souhaitez accéder n'existe plus.")
		context['eleve_list'] = eleves
		return context

@method_decorator(login_required, name='dispatch')
class ClasseCreate(generic.edit.CreateView):
	""" Create Classe """
	model = Classe
	fields = ['nom', 'cycle']

@method_decorator(login_required, name='dispatch')
class ClasseUpdate(generic.edit.UpdateView):
	""" Update Classe """
	model = Classe
	fields = ['nom', 'cycle']
	template_name_suffix = '_update_form'

@method_decorator(login_required, name='dispatch')
class ClasseDelete(generic.edit.DeleteView):
	""" Delete Classe """
	model = Classe
	success_url = reverse_lazy('gestion:classe_list')

# ELEVE Views
@method_decorator(login_required, name='dispatch')
class EleveDetail(generic.DetailView):
	""" Detail Eleve view """
	model = Eleve
	template_name = 'gestion/eleve_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		try:
			classe = Classe.objects.get(pk=context['eleve'].classe_id)
		except Classe.DoesNotExist:
			raise Http404("L'object auquel vous souhaitez accéder n'existe plus.")
		context['classe'] = classe
		return context

@method_decorator(login_required, name='dispatch')
class EleveCreate(generic.edit.CreateView):
	""" Create Eleve """
	model = Eleve
	fields = ['nom', 'prenom', 'classe']

@method_decorator(login_required, name='dispatch')
class EleveUpdate(generic.edit.UpdateView):
	""" Update Eleve """
	model = Eleve
	fields = ['nom', 'prenom', 'classe']
	template_name_suffix = '_update_form'

@method_decorator(login_required, name='dispatch')
class EleveDelete(generic.edit.DeleteView):
	""" Delete Eleve """
	model = Eleve
	success_url = reverse_lazy('gestion:classe_detail')

@method_decorator(login_required, name='dispatch')
class DomaineListView(generic.ListView):
	model = Domaine
	context_object_name = 'domaine_list'

	def get_queryset(self):
		cycle = None
		if self.kwargs['cycle'] == 'cycle3':
			cycle = 'Cycle 3'
		elif self.kwargs['cycle'] == 'cycle4':
			cycle = 'Cycle 4'
		else:
			raise Http404("La page que vous essayez d'atteindre n'existe pas.")
		return Domaine.objects.filter(cycle=cycle, sous_domaine_id=None).order_by('ref')
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cycle = None
		if self.kwargs['cycle'] == 'cycle3':
			cycle = 'Cycle 3'
		elif self.kwargs['cycle'] == 'cycle4':
			cycle = 'Cycle 4'
		context['cycle'] = cycle
		context['urlCycle'] = self.kwargs['cycle']
		return context

@method_decorator(login_required, name='dispatch')
class DomaineDetail(generic.DetailView):
	model = Domaine
	template_name = "gestion/domaine_detail.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		try:
			current_domaine = Domaine.objects.get(pk=context['domaine'].id)
			current_cycle = current_domaine.cycle
			urlCycle = None
			if current_cycle == 'Cycle 3':
				urlCycle = 'cycle3'
			elif current_cycle == 'Cycle 4':
				urlCycle = 'cycle4'
		except Domaine.DoesNotExist:
			raise Http404("L'object auquel vous souhaitez accéder n'existe plus.")

		domaine_list = []
		# On cherche les sous_domaines
		sous_domaines = Domaine.objects.filter(sous_domaine_id=context['domaine'].pk)

		if len(sous_domaines) > 0:
			# On parcours le QuerySet
			for s in sous_domaines:
				# On ajoute le sous_domaine a la liste
				domaine_list.append(s)
				# On recupere les Competences du sous_domaine
				competences = Competence.objects.filter(domaine_id=s.id)
				# On parcours le QuerySet
				for c in competences:
					# On ajoute les Competences
					domaine_list.append(c)

		else:
			# On recupere les Competences
			competences = Competence.objects.filter(domaine_id=context['domaine'].pk)
			domaine_list=competences

		context['domaine_CT_list'] = domaine_list
		context['domaine'] = current_domaine
		context['cycle'] = current_cycle
		context['urlCycle'] = urlCycle

		context['sous_domaines'] = Domaine.objects.filter(sous_domaine_id=context['domaine'].pk)
		context['sous_competences'] = Competence.objects.filter(domaine_id=context['domaine'].pk)
		return context

@method_decorator(login_required, name='dispatch')
class DomaineCreate(generic.edit.CreateView):
	""" Create Domaine """
	model = Domaine
	fields = ['ref', 'description', 'cycle']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cycle = None
		if self.kwargs['cycle'] == 'cycle3':
			cycle = 'Cycle 3'
		elif self.kwargs['cycle'] == 'cycle4':
			cycle = 'Cycle 4'
		context['urlCycle'] = self.kwargs['cycle']
		context['cycle'] = cycle
		return context

@method_decorator(login_required, name='dispatch')
class DomaineUpdate(generic.edit.UpdateView):
	""" Update Domaine """
	model = Domaine
	fields = ['ref', 'description', 'cycle']
	template_name_suffix = '_update_form'
	

@method_decorator(login_required, name='dispatch')
class DomaineDelete(generic.edit.DeleteView):
	""" Delete Domaine """
	model = Domaine
	success_url = reverse_lazy('gestion:domaine_list', kwargs={'cycle': 'cycle3'})

@method_decorator(login_required, name='dispatch')
class CompetenceCreate(generic.edit.CreateView):
	""" Create Competence """
	fields = ['ref', 'description', 'domaine']
	model = Competence

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cycle = None
		if self.kwargs['cycle'] == 'cycle3':
			cycle = 'Cycle 3'
		elif self.kwargs['cycle'] == 'cycle4':
			cycle = 'Cycle 4'
		context['urlCycle'] = self.kwargs['cycle']
		context['cycle'] = cycle
		return context

@method_decorator(login_required, name='dispatch')
class CompetenceUpdate(generic.edit.UpdateView):
	""" Update Competence """
	model = Competence
	fields = ['ref', 'description', 'cycle']
	template_name_suffix = '_update_form'
	

@method_decorator(login_required, name='dispatch')
class CompetenceDelete(generic.edit.DeleteView):
	""" Delete Competence """
	model = Competence
	success_url = reverse_lazy('gestion:domaine_list', kwargs={'cycle': 'cycle3'})


def homeView(request):
	""" Home view """
	return render(request, 'gestion/home.html')

def domaineCTUpdateRedirect(request, id):
	try:
		domaine = Domaine.objects.get(pk=id)
	except Domaine.DoesNotExist:
		domaine = None
	try:
		competence = Competence.objects.get(pk=id)
	except Competence.DoesNotExist:
		competence = None

	cycle = None
	if domaine != None:
		if domaine.cycle == 'Cycle 4':
			cycle = 'cycle4'
		else:
			cycle = 'cycle3'
		return redirect('gestion:update_domaine', cycle = cycle, pk = domaine.id)
	elif competence != None:
		if competence.cycle == 'Cycle 4':
			cycle = 'cycle4'
		else:
			cycle = 'cycle3'
		return redirect('gestion:update_competence', cycle = cycle, pk = competence.id)

def domaineCTDeleteRedirect(request, id):
	try:
		domaine = Domaine.objects.get(pk=id)
	except Domaine.DoesNotExist:
		domaine = None
	try:
		competence = Competence.objects.get(pk=id)
	except Competence.DoesNotExist:
		competence = None

	cycle = None
	if domaine != None:
		if domaine.cycle == 'Cycle 4':
			cycle = 'cycle4'
		else:
			cycle = 'cycle3'
		return redirect('gestion:delete_domaine', cycle = cycle, pk = domaine.id)
	elif competence != None:
		if competence.cycle == 'Cycle 4':
			cycle = 'cycle4'
		else:
			cycle = 'cycle3'
		return redirect('gestion:delete_competence', cycle = cycle, pk = competence.id)


"""
Domaine s'ajoute avec cycle
Sous domaine s'ajoute avec domaine_id filtrée par cycle
compétences s'ajout par domaine_id filtrée par cycle
"""

# class EleveListView(generic.ListView):
# 	template_name = 'gestion/eleve_list.html'
# 	context_object_name = 'eleve_list'

# 	def get_queryset(self):
# 		if classe_id != None:
# 			eleve_list = Eleve.objects.filter(classe_id=classe_id).order_by('nom')
# 		else:
# 			eleve_list = Eleve.objects.all().order_by('nom')
# 		return eleve_list

# def eleveList(request, classe_id=None):
# 	# On recupere la liste de classe pour le select

# 	if classe_id != None:
# 		current_classe = Classe.objects.get(pk=classe_id)
# 		eleve_list = Eleve.objects.filter(classe_id=classe_id).order_by('nom')
# 	else:
# 		current_classe = None
# 		eleve_list = Eleve.objects.all().order_by('nom')

# 	context = { 
# 		'eleve_list': eleve_list,
# 		'current_classe': current_classe,
# 		}
# 	return render(request, 'gestion/eleve_list.html', context)