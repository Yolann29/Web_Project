from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import json
from django.shortcuts import render
from .forms import SelectCompanyForm
from .models import cmp, advertisement, companies, permissions

class Inscription(View):
    def post(self, request, *args, **kwargs):
        corps_de_la_requete = json.loads(request.body.decode('utf-8'))
        surname = corps_de_la_requete.get('surname')
        first_name = corps_de_la_requete.get('first_name')
        username = corps_de_la_requete.get('username')
        password = corps_de_la_requete.get('password')
        email = corps_de_la_requete.get('email') 
        selected_company_id = corps_de_la_requete.get('companies')  
        try:
            selected_company = companies.objects.get(id=selected_company_id)
        except companies.DoesNotExist:
            return JsonResponse({'message': 'Entreprise non trouvée'}, status=400)
        nouvel_utilisateur = cmp(surname=surname, first_name=first_name, username=username, password=password, email=email, companies=selected_company)
        nouvel_utilisateur.save()
        nouvel_utilisateur.permissions = permissions.objects.get(id=2)
        nouvel_utilisateur.save()
        return JsonResponse({'message': 'Reçu !'})
    
class Connexion(View):
    def post(self, request, *args, **kwargs):
        corps_de_la_requete = json.loads(request.body.decode('utf-8'))
        username = corps_de_la_requete.get('username')
        password = corps_de_la_requete.get('password')
        try:
            utilisateur = cmp.objects.get(username=username, password=password)
            return JsonResponse({'message': 'Connecté !',
                                 'username': utilisateur.username,
                                 'permissions': utilisateur.permissions_id})
        except cmp.DoesNotExist:
            return JsonResponse({'message': 'Non connecté !'}, status=401)

class NewOffer(View):
    def post(self, request, *args, **kwargs):
        corps_de_la_requete = json.loads(request.body.decode('utf-8'))
        name = corps_de_la_requete.get('name')
        description = corps_de_la_requete.get('description')
        companie_existante = companies.objects.get(id=1)
        new_advertisement = advertisement(title=name, description=description, companies=companie_existante)
        new_advertisement.save()
        return JsonResponse({'message': 'Reçu !'})

def get_companies(request):
    companies_list = companies.objects.order_by('name').values('id', 'name')
    return JsonResponse(list(companies_list), safe=False)