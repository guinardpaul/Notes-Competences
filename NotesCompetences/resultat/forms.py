from django import forms
from gestion.models import Competence, EnumCycle, Classe
from .models import Evaluation
from django.db.models import Q

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
		