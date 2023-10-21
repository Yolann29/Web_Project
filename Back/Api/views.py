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


@api_view(['PUT'])
def ModAnn(request):
    if request == 'PUT':
        data = json.loads(request.body)
        annonce = advertisement.objects.get(id=data.id)
        annonce.title = data['title'],
        annonce.description = data['description'],
        annonce.save()
        return Response("Success")
    if request == 'DELETE':
        data = json.loads(request.body)
        annonce = advertisement.objects.get(id=data.id)
        annonce.delete()
        return Response("Success")
    else:
        return Response("Unknown method")


@api_view(['POST'])
def AddJobApp(request):
    data = json.loads(request.body)
    print("ici")
    modele_instance = JobApplication(
        applicant = cmp.objects.get(username=data['applicant']),
        advert = data['advert'],
        surname = data['surname'],
        first_name = data['first_name'],
        email = data['email']
    )
    modele_instance.save()
    return Response("Success")


@api_view(['PUT','DELETE'])
def ModJobApp(request):
    if request == 'PUT':
        data = json.loads(request.body)
        job_app = JobApplication.objects.get(advert=data.id)
        print(job_app)
        job_app.surname = data['surname']
        job_app.first_name = data['first_name']
        job_app.email = data['email']
        job_app.save()
        return Response("Success")
    if request == 'DELETE':
        data = json.loads(request.body)
        job_app = JobApplication.objects.get(id=data.id)
        job_app.delete()
        return Response("Success")
    else:
        return Response("Unknown method")


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
    
    return Response(rep)
    