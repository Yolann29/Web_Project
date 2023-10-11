from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import json
from .models import cmp

class Inscription(View):
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
    
class Connexion(View):
    def post(self, request, *args, **kwargs):
        corps_de_la_requete = json.loads(request.body.decode('utf-8'))
        username = corps_de_la_requete.get('username')
        password = corps_de_la_requete.get('password')

        # Recherche dans votre table 'utilisateur'
        try:
            utilisateur = cmp.objects.get(username=username, password=password)
            # Ici, vous pouvez faire quelque chose avec l'utilisateur authentifié.
            # Notez que cette manière de faire n'est pas sécurisée car le mot de passe doit être stocké en clair.
            return JsonResponse({'message': 'Connecté !'})
        except cmp.DoesNotExist:
            return JsonResponse({'message': 'Non connecté !'}, status=401)
