from django.urls import path
from . import views

urlpatterns = [
    path("", views.GetAnn),
    path("apply", views.AddJobApp),
    path("job", views.GetJobApply),
]