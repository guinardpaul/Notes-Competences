from django import forms
from .models import Competence, Domaine, EnumCycle, Classe
from resultat.models import Evaluation
from django.db.models import Q

class CompetenceForm(forms.ModelForm):
	"""docstring for CompetenceForm"""
	class Meta:
		model = Competence
		fields = ['ref', 'description', 'domaine']

	def __init__(self, *args, **kwargs):
		current_domaine_id = kwargs.pop('domaine_id')
		# On filtre le select domaine
		domaine_choices = None
		# S'il contient des sous_domaines, on montre les sous_domaines
		if len(Domaine.objects.filter(sous_domaine=current_domaine_id)) > 0:
			domaine_choices = Domaine.objects.filter(sous_domaine=current_domaine_id)
		# S'il n'y a pas de sous_domaines, on montre le domaine
		else:
			domaine_choices = Domaine.objects.filter(id=current_domaine_id)

		super(CompetenceForm, self).__init__(*args, **kwargs)
		self.fields['domaine'].queryset = domaine_choices

class SousDomaineForm(forms.ModelForm):
	"""docstring for CompetenceForm"""
	class Meta:
		model = Domaine
		fields = ['ref', 'description', 'sous_domaine']


	def __init__(self, *args, **kwargs):
		# cycle = kwargs.pop('cycle')
		current_domaine_id = kwargs.pop('domaine_id')
		# if cycle == 'cycle4':
		# 	cycle = 'Cycle 4'
		# else:
		# 	cycle = 'Cycle 3'
		super(SousDomaineForm, self).__init__(*args, **kwargs)
		self.fields['sous_domaine'].label = 'Domaine'
		self.fields['sous_domaine'].required=True
		self.fields['sous_domaine'].queryset = Domaine.objects.filter(id=current_domaine_id)

class EvaluationForm(forms.ModelForm):
	class Meta:
		model = Evaluation
		fields = ['description', 'trimestre', 'classe', 'competence', 'cycle']
		
	def __init__(self, *args, **kwargs):
		current_cycle = EnumCycle.objects.get(literal=kwargs.pop('cycle'))
		#print(current_cycle)
		# On filtre le select competences
		competence_choices = None
		competence_choices = Competence.objects.filter(cycle=current_cycle)

		super(EvaluationForm, self).__init__(*args, **kwargs)
		self.fields['competence'].label = 'Competences %s' % current_cycle.literal
		self.fields['competence'].queryset = competence_choices
		self.fields['classe'].queryset = Classe.objects.filter(cycle=current_cycle)
		self.fields['cycle'].label = ''
		self.fields['cycle'].widget = forms.HiddenInput()
		self.fields['cycle'].initial = current_cycle
		