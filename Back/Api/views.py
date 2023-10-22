from rest_framework.response import Response
from rest_framework.decorators import api_view
from utilisateur.models import advertisement, JobApplication, companies, cmp, permissions
from Api.serializers import AnnonceSerializer, CompaniesSerializer, JobApplicationSerializer, CmpSerializer
from Api.serializers import AnnonceSerializer, CompaniesSerializer, JobApplicationSerializer, JobAppCustomSerializer
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
        utilisateur.permissions = permissions.objects.get(id=data['permissions'])
        utilisateur.companies = companies.objects.get(id=data['companies'])
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
        annonce.title = data['title']
        annonce.description = data['description']
        if 'cmp' in data:
            annonce.cmp = cmp.objects.get(id=data['cmp'])
        if 'companies' in data:
            annonce.companies = companies.objects.get(id=data['companies'])
        annonce.save()
        return Response("Success")
    if request.method == 'DELETE':
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
        if 'advert' in data:
            job_app.advert = companies.objects.get(id=data['advert'])
        if 'applicant' in data:
            job_app.applicant = companies.objects.get(id=data['applicant'])
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


@api_view(['POST'])
def GetJobApply(request):
    data = json.loads(request.body)
    cmpname = cmp.objects.get(username = data['applicant'])
    postulate = JobApplication.objects.filter(applicant=cmpname.id)
    for pos in postulate:
        pos.title = pos.advert.title
        ad_comp = pos.advert.companies
        pos.company = ad_comp.name
    serializer = JobAppCustomSerializer(postulate, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def DeleteJobApply(request, article_id):
    article = JobApplication.objects.get(id=article_id)
    article.delete()
    return Response("success")

@api_view(['POST'])
def AffichageMyAds(request):
    data = json.loads(request.body)
    utilisateur = cmp.objects.get(username=data['username'])
    ads = advertisement.objects.filter(cmp=utilisateur.id)
    serializer = AnnonceSerializer(ads, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def AffichageJobApps(request):
    data = json.loads(request.body)
    print(data)
    job_apps = JobApplication.objects.filter(advert=data['id'])
    print(job_apps)
    serializer = JobApplicationSerializer(job_apps, many=True)
    return Response(serializer.data)