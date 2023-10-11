from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import json
from .models import cmp

# Create your views here.
class MaVue(View):
    def post(self, request, *args, **kwargs):
        corps_de_la_requete = json.loads(request.body.decode('utf-8'))
        surname = corps_de_la_requete.get('surname')
        first_name = corps_de_la_requete.get('first_name')
        username = corps_de_la_requete.get('username')
        password = corps_de_la_requete.get('password')
        email = corps_de_la_requete.get('email')   
        nouvel_utilisateur = cmp(surname=surname, first_name=first_name, username=username, password=password, email=email)
        nouvel_utilisateur.save()
        return JsonResponse({'message': 'Reçu !'})