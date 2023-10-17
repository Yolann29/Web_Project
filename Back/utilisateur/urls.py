from django.urls import path
from . import views
from django.middleware.csrf import get_token

urlpatterns = [
    path('register', views.Inscription.as_view(), name="ma_vue"),
    path('login', views.Connexion.as_view(), name='login'),
    path('newoffer', views.NewOffer.as_view(), name='newoffer'),
    path('companies', views.get_companies, name='get_companies'),
]