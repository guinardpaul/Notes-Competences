from django.urls import path

from . import views

app_name = 'resultat'
urlpatterns = [
    # Home
    path('', views.homeView, name="home"),
    path('add/<slug:cycle>/', views.evaluationCreate, name="add_evaluation"),
]
