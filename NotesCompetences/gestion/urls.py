from django.urls import path

from . import views

app_name = 'gestion'
urlpatterns = [
    # Home
    path('', views.homeView, name="home"),
	# Classe urls
    path('classe/', views.ClasseListView.as_view(), name="classe_list"),
    path('classe/<int:pk>', views.ClasseDetail.as_view(), name="classe_detail"),
    path('classe/add', views.ClasseCreate.as_view(), name="add_classe"),
    path('classe/update/<int:pk>', views.ClasseUpdate.as_view(), name="update_classe"),
    path('classe/delete/<int:pk>', views.ClasseDelete.as_view(), name="delete_classe"),
    # Eleve urls
    path('eleve/<int:pk>', views.EleveDetail.as_view(), name="eleve_detail"),
    path('eleve/add', views.EleveCreate.as_view(), name="add_eleve"),
    path('eleve/update/<int:pk>', views.EleveUpdate.as_view(), name="update_eleve"),
    path('eleve/delete/<int:pk>', views.EleveDelete.as_view(), name="delete_eleve"),
    # Domaine urls
    path('domaine/cycle3', views.DomaineCycle3ListView.as_view(), name="domaine_list_cycle3"),
    path('domaine/cycle4', views.DomaineCycle4ListView.as_view(), name="domaine_list_cycle4"),
    # Competence urls
    path('domaine/detail/<int:pk>', views.DomaineDetail.as_view(), name="domaine_detail"),
    # Login
    #path('login/', views.login, name="login"),
]
