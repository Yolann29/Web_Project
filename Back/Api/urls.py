from django.urls import path
from . import views

urlpatterns = [
    path("", views.GetData),
    # path("add/", views.AddData),
]