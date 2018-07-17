from django.urls import path

from . import views

app_name = 'resultat'
urlpatterns = [
    # Home
    path('', views.homeView, name="home"),
    # ===== A enlever ==========
    path('add/<slug:cycle>/', views.evaluationCreate, name="add_evaluation"),
    path('update/<int:pk>', views.EvaluationUpdate.as_view(), name="update_evaluation"),
    path('delete/<int:pk>', views.EvaluationDelete.as_view(), name="delete_evaluation"),
    # ========

    # path('add/<slug:cycle>/', views.ResultatCreate, name="add_resultat"),
    # path('update/<int:pk>', views.ResultatUpdate.as_view(), name="update_resultat"),
    # path('delete/<int:pk>', views.ResultatDelete.as_view(), name="delete_resultat"),
]
