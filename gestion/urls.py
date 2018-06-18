from django.urls import path

from . import views

app_name = 'gestion'
urlpatterns = [
    path('classe/', views.ClasseListView.as_view(), name="classe_list"),
    path('classe/add', views.ClasseCreate.as_view(), name="add_classe"),
    path('classe/update/<int:pk>', views.ClasseUpdate.as_view(), name="update_classe"),
    path('classe/delete/<int:pk>', views.ClasseDelete.as_view(), name="delete_classe"),
    path('eleve/', views.eleveList, name="eleve_list"),
    path('eleve/<int:classe_id>', views.eleveList, name="eleve_list_filtered"),
    path('eleve/add', views.EleveCreate.as_view(), name="add_eleve"),
    path('eleve/update/<int:pk>', views.EleveUpdate.as_view(), name="update_eleve"),
    path('eleve/delete/<int:pk>', views.EleveDelete.as_view(), name="delete_eleve"),
]