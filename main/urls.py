from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('home/', views.home, name = "home"),
    path('sign-up/', views.signup, name = "sign-up"),
    path('sign-in/', views.login, name = "sign-in"),
    path('sign-up-sucess/', views.signsuccess, name = "sign-up-sucess"),
    path('password-reset/', views.Passwordreset, name = "password-reset"),
]