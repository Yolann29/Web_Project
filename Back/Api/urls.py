from django.urls import path
from . import views

urlpatterns = [
    path("", views.GetAnn),
    path("apply", views.AddJobApp),
    path("modUser", views.ModUser),
    path("modAnn", views.ModAnn),
    path("modJobApp", views.ModJobApp),
    path("modComp", views.ModComp),
    path("superadmin", views.AdminAffichage),
    path("job", views.GetJobApply),
    path("delete_apply/<int:article_id>/", views.DeleteJobApply),
    path("myads", views.AffichageMyAds),
    path("myapps", views.AffichageJobApps),
    
]