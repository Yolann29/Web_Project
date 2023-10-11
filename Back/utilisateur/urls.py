from django.urls import path
from . import views
from django.middleware.csrf import get_token

urlpatterns = [
    path('', views.MaVue.as_view(), name="ma_vue"),
]