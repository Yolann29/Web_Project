from django.urls import path
from . import views

urlpatterns = [
    path("", views.GetAnn),
    path("apply", views.AddJobApp),
    path("modJobApp", views.ModJobApp),
    path("modAnn", views.ModAnn),
    path("superadmin", views.AdminAffichage)
]