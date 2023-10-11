from django.urls import path

from . import views

urlpatterns = [
    path("recup", views.recup, name="recup"),
    path("home", views.home, name="home"),
]