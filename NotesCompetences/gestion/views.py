from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Classe, Eleve, Domaine, Competence
from itertools import chain
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
		context['eleve_list'] = Eleve.objects.filter(classe=context['classe'].id)
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
		context['classe'] = Classe.objects.get(pk=context['eleve'].classe_id)
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
class DomaineCycle3ListView(generic.ListView):
	""" Liste des domaines du cycle 3 """
	model = Domaine
	context_object_name = 'domaine_list'

	def get_queryset(self):
		return Domaine.objects.filter(cycle='Cycle 3').order_by('ref')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['cycle'] = "Cycle 3"
		return context

@method_decorator(login_required, name='dispatch')
class DomaineCycle4ListView(generic.ListView):
	""" Liste des domaines du cycle 4 """
	model = Domaine
	context_object_name = 'domaine_list'

	def get_queryset(self):
		return Domaine.objects.filter(cycle='Cycle 4').order_by('ref')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['cycle'] = "Cycle 4"
		return context

class DomaineDetail(generic.DetailView):
	model = Domaine
	template_name = "gestion/domaine_detail.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		domaine_list = []
		sous_domaines = Competence.objects.filter(ref__startswith="D", domaine_id=context['domaine'].pk)
		print('Sous-domaines :%s' % sous_domaines)
		if len(sous_domaines) > 0:
			print('boucle')
			for s in sous_domaines:
				domaine_list.append(s)
				# Changer pk du domaine par pk du sous-domaines.
				# Nécessite de changer la facon d'enregistrer les models
				competences = Competence.objects.filter(ref__startswith="CT", domaine_id=context['domaine'].pk)
				# domaine_list=list(chain((s,competences)))
				for c in competences:
					domaine_list.append(c)

				print('domaine_list %s' % domaine_list)
		else:
			competences = Competence.objects.filter(ref__startswith="CT", domaine_id=context['domaine'].pk)
			domaine_list=(competences)

		print('domaine_list: %s' % domaine_list)
		context['domaine_list'] = domaine_list
		context['sous_domaines'] = Competence.objects.filter(ref__startswith="D", domaine_id=context['domaine'].pk)
		context['sous_competences'] = Competence.objects.filter(ref__startswith="CT", domaine_id=context['domaine'].pk)
		return context

def homeView(request):
	""" Home view """
	return render(request, 'gestion/home.html')

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