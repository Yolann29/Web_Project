from rest_framework.response import Response
from rest_framework.decorators import api_view
from utilisateur.models import advertisement, JobApplication, companies, cmp
from Api.serializers import AnnonceSerializer, CompaniesSerializer, JobApplicationSerializer, CmpSerializer
import json


@api_view(['GET'])
def GetAnn(request):
    annonces = advertisement.objects.all()
    serializer = AnnonceSerializer(annonces, many=True)
    for data in serializer.data:
        c_id = data.get("companies")
        if c_id is not None:
            company = companies.objects.get(id=c_id)
            company_data = CompaniesSerializer(company).data
            data['companies'] = company_data.get('name')
        else:
            data['companies'] = None
    return Response(serializer.data)


@api_view(['POST'])
def AddJobApp(request):
    data = json.loads(request.body)
    advert_instance = advertisement.objects.get(id=data['advert'])
    modele_instance = JobApplication(
        applicant = cmp.objects.get(username=data['applicant']),
        advert = advert_instance,
        surname = data['surname'],
        first_name = data['first_name'],
        email = data['email']
    )
    modele_instance.save()
    return Response("Success")


@api_view(['GET'])
def AdminAffichage(request):
    rep = []
    
    cmps = cmp.objects.all()
    sercmps = CmpSerializer(cmps, many=True)
    rep.append(sercmps.data)
    
    ads = advertisement.objects.all()
    serads = AnnonceSerializer(ads, many=True)
    rep.append(serads.data)
    
    jobapps = JobApplication.objects.all()
    serjobapps = JobApplicationSerializer(jobapps, many=True)
    rep.append(serjobapps.data)
    
    comps = companies.objects.all()
    sercomps = CompaniesSerializer(comps, many=True)
    rep.append(sercomps.data)
    print(rep)
    return Response(rep)


@api_view(['PUT','DELETE'])
def ModUser(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        utilisateur = cmp.objects.get(id=data['id'])
        print(utilisateur)
        utilisateur.surname = data['surname']
        utilisateur.first_name = data['first_name']
        utilisateur.username = data['username']
        utilisateur.password = data['password']
        utilisateur.email = data['email']
        utilisateur.permissions = data['permissions']
        utilisateur.companies = data['companies']
        utilisateur.save()
        return Response("Success")
    if request.method == 'DELETE':
        data = json.loads(request.body)
        utilisateur = cmp.objects.get(id=data['id'])
        utilisateur.delete()
        return Response("Success")
    else:
        return Response("Unknown method")


@api_view(['PUT','DELETE'])
def ModAnn(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        annonce = advertisement.objects.get(id=data['id'])
        annonce.title = data['title'],
        annonce.description = data['description'],
        annonce.cmp = data['cmp'],
        annonce.companies = data['companies'],
        annonce.save()
        return Response("Success")
    if request.method == 'DELETE':
        print("ici")
        data = json.loads(request.body)
        annonce = advertisement.objects.get(id=data['id'])
        annonce.delete()
        return Response("Success")
    else:
        return Response("Unknown method")


@api_view(['PUT','DELETE'])
def ModJobApp(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        job_app = JobApplication.objects.get(id=data['id'])
        job_app.surname = data['surname']
        job_app.first_name = data['first_name']
        job_app.email = data['email']
        job_app.save()
        return Response("Success")
    if request.method == 'DELETE':
        data = json.loads(request.body)
        job_app = JobApplication.objects.get(id=data['id'])
        job_app.delete()
        return Response("Success")
    else:
        return Response("Unknown method")


@api_view(['PUT','DELETE'])
def ModComp(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        company = companies.objects.get(id=data['id'])
        print(company)
        company.name = data['name']
        company.save()
        return Response("Success")
    if request.method == 'DELETE':
        data = json.loads(request.body)
        company = companies.objects.get(id=data['id'])
        company.delete()
        return Response("Success")
    else:
        return Response("Unknown method")
    