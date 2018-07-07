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
def homeView(request):
	return render(request, 'resultat/home.html')

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
			print(form.cleaned_data)
			form.cleaned_data['cycle'] = literal_cycle
			new_evaluation = form.save()

			return HttpResponseRedirect('/results')
	else:
		form = EvaluationForm(cycle=literal_cycle)

	return render(request, 'resultat/evaluation_form.html', {'form': form, 'cycle': literal_cycle})