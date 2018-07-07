from django import forms
from gestion.models import Competence, EnumCycle
from .models import Evaluation
from django.db.models import Q

class EvaluationForm(forms.ModelForm):
	class Meta:
		model = Evaluation
		fields = ['description', 'trimestre', 'competence']

	def __init__(self, *args, **kwargs):
		current_cycle = EnumCycle.objects.get(literal=kwargs.pop('cycle'))
		#print(current_cycle)
		# On filtre le select competences
		competence_choices = None
		competence_choices = Competence.objects.filter(cycle=current_cycle)

		super(EvaluationForm, self).__init__(*args, **kwargs)
		self.fields['competence'].label = 'Competences ' + current_cycle.literal
		self.fields['competence'].queryset = competence_choices
		