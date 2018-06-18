from django.urls import path

from . import views

app_name = 'classe'
urlpatterns = [
    path('', views.index, name="index"),
]
