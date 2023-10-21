from django.urls import path
from . import views

urlpatterns = [
    path("", views.GetAnn),
    path("apply", views.AddJobApp),
    path("modApp", views.ModJobApp),
    path("modAnn", views.ModAnn),
    path("superadmin", views.AdminAffichage)
]