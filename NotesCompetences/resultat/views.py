from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import EvaluationForm
from .models import Evaluation
from gestion.models import EnumCycle

# Create your views here.
@login_required
def homeView(request):
	evaluations = Evaluation.objects.all()

	return render(request, 'resultat/home.html', { 'evaluations': evaluations })

@login_required
def evaluationCreate(request, cycle):
	literal_cycle = None
	if cycle == 'cycle3':
		literal_cycle = 'Cycle 3'
	elif cycle == 'cycle4':
		literal_cycle = 'Cycle 4'
	else:
		raise Http404("La page que vous souhaitez atteindre n'existe pas.")

	if request.method == 'POST':
		form = EvaluationForm(request.POST, cycle=literal_cycle)
		if form.is_valid():
			new_evaluation = form.save()

			return HttpResponseRedirect('/results')
	else:
		form = EvaluationForm(cycle=literal_cycle)

	return render(request, 'resultat/evaluation_form.html', {'form': form, 'cycle': literal_cycle})

@method_decorator(login_required, name='dispatch')
class EvaluationUpdate(generic.edit.UpdateView):
	""" Update Evaluation """
	model = Evaluation
	fields = ['description', 'trimestre', 'classe', 'competence', 'cycle']
	template_name_suffix = '_update_form'

@method_decorator(login_required, name='dispatch')
class EvaluationDelete(generic.edit.DeleteView):
	""" Delete Evaluation """
	model = Evaluation
	success_url = reverse_lazy('resultat:home')