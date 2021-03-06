from django.urls import path

from . import views

app_name = 'authentication'
urlpatterns = [
    #
    path('profile/', views.profileView, name="profile"),
    # NOT USED
    path('sign-in/', views.UserSignInView.as_view(), name="sign-in"),
    path('sign-up/', views.UserSignUpView.as_view(), name="sign-up"),
]
