from django import forms
from .models import Competence, Domaine

class CompetenceForm(forms.ModelForm):
	"""docstring for CompetenceForm"""
	class Meta:
		model = Competence
		fields = ['ref', 'description', 'domaine']

	def __init__(self, competence, *args, **kwargs):
		super(CompetenceForm, self).__init__(competence, *args, **kwargs)
		self.fields['domaine'].queryset = Domaine.objects.filter(cycle=competence.cycle)
