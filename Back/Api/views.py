from rest_framework.response import Response
from rest_framework.decorators import api_view
from utilisateur.models import advertisement, JobApplication, companies, cmp
from Api.serializers import AnnonceSerializer, CompaniesSerializer, JobApplicationSerializer
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

@api_view(['GET'])
def GetJobAd(request):
    data = json.loads(request.body)
    print(data)
    utilisateur = cmp.objects.get(username=data['username'])
    print(utilisateur)
    ads = advertisement.objects.filter(cmp=utilisateur.id)
    print(ads)
    rep = None
    for ad in ads:
        job_ads = JobApplication.objects.filter(advert=ad.id)
        serializer = JobApplicationSerializer(job_ads, many=True)
        rep = rep + serializer.data
        print(rep)
    return Response(rep)

@api_view(['POST'])
def AddJobApp(request):
    data = json.loads(request.body)
    modele_instance = JobApplication(
        company = companies.objects.get(name=data['company']),
        applicant = cmp.objects.get(username=data['applicant']),
        advert = data['advert'],
        surname = data['surname'],
        first_name = data['first_name'],
        email = data['email']
    )
    modele_instance.save()
    return Response(data)

@api_view(['PUT'])
def ModAnn(request):
    data = json.loads(request.body)
    annonce = advertisement.objects.get(id=data.id)
    modele_instance = advertisement(
        title = data['title'],
        description = data['description'],
        cmp = cmp.objects.get(username=data['useername']),
    )
    modele_instance.save()
    serializer = AnnonceSerializer(annonce)
    return Response(serializer.data)