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
    path('domaine/<slug:cycle>', views.DomaineListView.as_view(), name="domaine_list"),
    path('domaine/detail/<int:pk>', views.DomaineDetail.as_view(), name="domaine_detail"),
    # path('domaine/cycle3', views.DomaineCycle3ListView.as_view(), name="domaine_list_cycle3"),
    # path('domaine/cycle4', views.DomaineCycle4ListView.as_view(), name="domaine_list_cycle4"),
    path('domaine/<slug:cycle>/add', views.DomaineCreate.as_view(), name="add_domaine"),
    path('domaine/<slug:cycle>/update/<int:pk>', views.DomaineUpdate.as_view(), name="update_domaine"),
    path('domaine/<slug:cycle>/delete/<int:pk>', views.DomaineDelete.as_view(), name="delete_domaine"),
    # SousDomaine urls
    path('domaine/<slug:cycle>/<int:domaine_id>/add', views.createSousDomaine, name="add_sous_domaine"),
    # path('competence/<slug:cycle>/add', views.CompetenceCreate.as_view(), name="add_competence"),
    # Competence urls
    path('competence/<slug:cycle>/<int:domaine_id>/add', views.createCompetence, name="add_competence"),
    path('competence/<slug:cycle>/update/<int:pk>', views.CompetenceUpdate.as_view(), name="update_competence"),
    path('competence/<slug:cycle>/delete/<int:pk>', views.CompetenceDelete.as_view(), name="delete_competence"),
    # Default url for update/delete Domaine - Competence table
    path('domaine/update/<int:id>', views.domaineCTUpdateRedirect, name="update_domaine_ct"),
    path('domaine/delete/<int:id>', views.domaineCTDeleteRedirect, name="delete_domaine_ct"),
    
]
