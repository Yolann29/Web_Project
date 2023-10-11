from django.shortcuts import render
from django.http import HttpResponse
from Compte.models import cmp

# Create your views here.

def recup(request):
    return HttpResponse("Bonjour Recup")

def home(request):
    people = cmp.objects.get(surname="Morellet")
    # return HttpResponse("Bonjour Home")
    return HttpResponse(people.username)