from django.shortcuts import render

from .models import Classe
# Create your views here.
def index(request):
	classe_list = Classe.objects.all()
	context = { 'classe_list': classe_list, 'nav_link': 'classe' }
	return render(request, 'classe/index.html', context)