from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Classe, Eleve, Domaine, Competence

# Create your views here.
class ClasseListView(generic.ListView):
	template_name = 'gestion/classe_list.html'
	context_object_name = 'classe_list'

	def get_queryset(self):
		return Classe.objects.all().order_by('cycle', 'nom')

class ClasseCreate(generic.edit.CreateView):
	model = Classe
	fields = ['nom', 'cycle']
	success_url = reverse_lazy('gestion:classe_list')

class ClasseUpdate(generic.edit.UpdateView):
	model = Classe
	fields = ['nom', 'cycle']
	template_name_suffix = '_update_form'
	success_url = reverse_lazy('gestion:classe_list')

class ClasseDelete(generic.edit.DeleteView):
	model = Classe
	success_url = reverse_lazy('gestion:classe_list')

# class EleveListView(generic.ListView):
# 	template_name = 'gestion/eleve_list.html'
# 	context_object_name = 'eleve_list'

# 	def get_queryset(self):
# 		if classe_id != None:
# 			eleve_list = Eleve.objects.filter(classe_id=classe_id).order_by('nom')
# 		else:
# 			eleve_list = Eleve.objects.all().order_by('nom')
# 		return eleve_list

def eleveList(request, classe_id=None):
	# On recupere la liste de classe pour le select
	classe_list = Classe.objects.all()

	if classe_id != None:
		current_classe = Classe.objects.get(pk=classe_id)
		eleve_list = Eleve.objects.filter(classe_id=classe_id).order_by('nom')
	else:
		current_classe = None
		eleve_list = Eleve.objects.all().order_by('nom')

	context = { 
		'eleve_list': eleve_list, 
		'classe_list': classe_list,
		'current_classe': current_classe,
		}

	return render(request, 'gestion/eleve_list.html', context)

class EleveCreate(generic.edit.CreateView):
	model = Eleve
	fields = ['nom', 'prenom', 'classe']
	success_url = reverse_lazy('gestion:eleve_list')

class EleveUpdate(generic.edit.UpdateView):
	model = Eleve
	fields = ['nom', 'prenom', 'classe']
	template_name_suffix = '_update_form'
	success_url = reverse_lazy('gestion:eleve_list')

class EleveDelete(generic.edit.DeleteView):
	model = Eleve
	success_url = reverse_lazy('gestion:eleve_list')

# def index(request):
# 	classe_list = Classe.objects.all()
# 	context = { 'classe_list': classe_list, 'nav_link': 'classe' }
# 	return render(request, 'gestion/index.html', context)