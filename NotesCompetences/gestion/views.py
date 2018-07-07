from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Classe, Eleve, Domaine, Competence, EnumCycle
from .forms import CompetenceForm, SousDomaineForm

# Create your views here.
# CLASSE Views
@method_decorator(login_required, name='dispatch')
class ClasseListView(generic.ListView):
	""" Affiche la liste des classes """
	template_name = 'gestion/classe_list.html'
	context_object_name = 'classe_list'

	# On recupere la liste des classes
	def get_queryset(self):
		return Classe.objects.all().order_by('cycle', 'nom')

@method_decorator(login_required, name='dispatch')
class ClasseDetail(generic.DetailView):
	""" Detail d'une classe avec les eleves """
	model = Classe
	template_name = 'gestion/classe_detail.html'

	# On recupere la liste des eleves de la classe
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		try:
			eleves = Eleve.objects.filter(classe=context['classe'].id).order_by('nom')
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

	# On recupere la classe et la passe au context
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

	# On retourne sur le classe_detail
	def get_success_url(self):
		return reverse_lazy('gestion:classe_detail', kwargs={'pk': self.object.classe_id})

@method_decorator(login_required, name='dispatch')
class DomaineListView(generic.ListView):
	""" Domaine List filtre par cycle """
	model = Domaine
	context_object_name = 'domaine_list'

	# On recupere les domaines filtres par cycle
	def get_queryset(self):
		cycle = None
		if self.kwargs['cycle'] == 'cycle3':
			cycle = EnumCycle.objects.get(literal='Cycle 3')
		elif self.kwargs['cycle'] == 'cycle4':
			cycle = EnumCycle.objects.get(literal='Cycle 4')
		else:
			raise Http404("La page que vous essayez d'atteindre n'existe pas.")
		return Domaine.objects.filter(cycle=cycle.id, sous_domaine_id=None).order_by('ref')
	
	# On recupere le cycle et le passe au context
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
	""" 
		Domaine detail
		Affiche le current_domaine, les sous_domaines (si existent) et les competences
	"""
	model = Domaine
	template_name = "gestion/domaine_detail.html"

	# On recupere le context
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		try:
			current_domaine = Domaine.objects.get(pk=context['domaine'].id)
			current_cycle = EnumCycle.objects.get(pk=current_domaine.cycle_id)
			urlCycle = None
			if current_cycle.literal == 'Cycle 3':
				urlCycle = 'cycle3'
			elif current_cycle.literal == 'Cycle 4':
				urlCycle = 'cycle4'
			else:
				raise Http404("La page que vous essayez d'atteindre n'existe pas.")
		except Domaine.DoesNotExist:
			raise Http404("L'object auquel vous souhaitez accéder n'existe plus.")

		domaine_list = []
		# On cherche les sous_domaines
		sous_domaines = Domaine.objects.filter(sous_domaine_id=context['domaine'].pk).order_by('ref')

		# Il y a des sous_domaines
		if len(sous_domaines) > 0:
			# On parcours le QuerySet
			for s in sous_domaines:
				# On ajoute le sous_domaine a la liste
				domaine_list.append(s)
				# On recupere les Competences du sous_domaine
				competences = Competence.objects.filter(domaine_id=s.id).order_by('ref')
				# On parcours le QuerySet
				for c in competences:
					# On ajoute les Competences
					domaine_list.append(c)
		# Il n'y a pas de sous_domaines
		else:
			# On recupere les Competences
			competences = Competence.objects.filter(domaine_id=context['domaine'].pk).order_by('ref')
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

	# On recupere le cycle et le passe au context
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cycle = None
		if self.kwargs['cycle'] == 'cycle3':
			cycle = 'Cycle 3'
		elif self.kwargs['cycle'] == 'cycle4':
			cycle = 'Cycle 4'
		else:
			raise Http404("La page que vous essayez d'atteindre n'existe pas.")
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
	
	# On recupere le cycle et le passe au context
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cycle = self.object.cycle
		urlCycle = None
		if cycle == 'Cycle 3':
			urlCycle = 'cycle3'
		else:
			urlCycle = 'cycle4'
		context['urlCycle'] = self.kwargs['cycle']
		context['cycle'] = cycle
		return context

	# On redirect sur domaine_list du cycle
	def get_success_url(self):
		cycle = self.object.cycle
		urlCycle = None
		if cycle == 'Cycle 3':
			urlCycle = 'cycle3'
		else:
			urlCycle = 'cycle4'

		return reverse_lazy('gestion:domaine_list', kwargs={ 'cycle': urlCycle })

@method_decorator(login_required, name='dispatch')
class CompetenceCreate(generic.edit.CreateView):
	""" 
		Not Used 
		Create Competence 
	"""
	fields = ['ref', 'description', 'domaine']
	model = Competence

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cycle = None
		if self.kwargs['cycle'] == 'cycle3':
			cycle = 'Cycle 3'
		elif self.kwargs['cycle'] == 'cycle4':
			cycle = 'Cycle 4'
		else:
			raise Http404("La page que vous essayez d'atteindre n'existe pas.")
		context['urlCycle'] = self.kwargs['cycle']
		context['cycle'] = cycle
		return context

@method_decorator(login_required, name='dispatch')
class CompetenceUpdate(generic.edit.UpdateView):
	""" Update Competence """
	model = Competence
	fields = ['ref', 'description']
	template_name_suffix = '_update_form'

	# On recupere le cycle pour le passer a la vue
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cycle = None
		if self.kwargs['cycle'] == 'cycle3':
			cycle = 'Cycle 3'
		elif self.kwargs['cycle'] == 'cycle4':
			cycle = 'Cycle 4'
		else:
			raise Http404("La page que vous essayez d'atteindre n'existe pas.")
		context['urlCycle'] = self.kwargs['cycle']
		context['cycle'] = cycle
		return context

@method_decorator(login_required, name='dispatch')
class CompetenceDelete(generic.edit.DeleteView):
	""" Delete Competence """
	model = Competence
	
	# On recupere le cycle pour le passer a la vue
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cycle = None
		if self.kwargs['cycle'] == 'cycle3':
			cycle = 'Cycle 3'
		elif self.kwargs['cycle'] == 'cycle4':
			cycle = 'Cycle 4'
		else:
			raise Http404("La page que vous essayez d'atteindre n'existe pas.")
		context['urlCycle'] = self.kwargs['cycle']
		context['cycle'] = cycle
		return context

	# On redirect au domaine_detail du domaine
	def get_success_url(self):
		sous_domaine = Domaine.objects.get(pk=self.object.domaine_id)
		try:
			domaine = Domaine.objects.get(pk=sous_domaine.sous_domaine_id)
		except Domaine.DoesNotExist:
			domaine = sous_domaine

		return reverse_lazy('gestion:domaine_detail', kwargs={ 'pk': domaine.pk })

def homeView(request):
	""" Home view """
	return render(request, 'gestion/home.html')

@login_required
def createCompetence(request, cycle, domaine_id):
	""" Create competence """
	if request.method == 'POST':
		form = CompetenceForm(request.POST, domaine_id=domaine_id)
		if form.is_valid():
			new_competence = form.save()

			return HttpResponseRedirect('/domaine/detail/' + str(domaine_id))
	else:
		form = CompetenceForm(domaine_id=domaine_id)

	return render(request, 'gestion/competence_form.html', {'form': form, 'cycle': cycle})

@login_required
def createSousDomaine(request, cycle, domaine_id):
	""" create sous domaine """
	warning_message = 'Attention. Si vous ajoutez un sous-domaine alors que des compétences existent déjà pour ce domaine, vous devrez recréer ces compétences.'
	
	if request.method == 'POST':
		form = SousDomaineForm(request.POST, domaine_id=domaine_id)
		if form.is_valid():
			new_sous_domaine = form.save()
			return HttpResponseRedirect('/domaine/detail/' + str(new_sous_domaine.sous_domaine.id))
	else:
		form = SousDomaineForm(domaine_id=domaine_id)

	return render(request, 'gestion/domaine_form.html', {'form': form, 'cycle': cycle, 'warning_message': warning_message})

@login_required
def domaineCTUpdateRedirect(request, id):
	""" Redirect to view to process Update on sous-domaine/competence table """
	# On recupere l'objet grace a son id
	try:
		domaine = Domaine.objects.get(pk=id)
	except Domaine.DoesNotExist:
		domaine = None
	try:
		competence = Competence.objects.get(pk=id)
	except Competence.DoesNotExist:
		competence = None

	# On recupere le cycle et redirect a la bonne vue suivant l'objet 
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

@login_required
def domaineCTDeleteRedirect(request, id):
	""" Redirect to view to process Delete on sous-domaine/competence table """
	# On recupere l'objet grace a son id
	try:
		domaine = Domaine.objects.get(pk=id)
	except Domaine.DoesNotExist:
		domaine = None
	try:
		competence = Competence.objects.get(pk=id)
	except Competence.DoesNotExist:
		competence = None

	# On recupere le cycle et redirect a la bonne vue suivant l'objet 
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
