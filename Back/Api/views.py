from rest_framework.response import Response
from rest_framework.decorators import api_view
from Adverts.models import Annonce, JobApplication, companies, cmp
from Api.serializers import AnnonceSerializer
import json

@api_view(['GET'])
def GetAnn(request):
    annonces = Annonce.objects.all()
    serializer = AnnonceSerializer(annonces, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def AddJobApp(request):
    data = json.loads(request.body)
    print(data)
    modele_instance = JobApplication(
        company = companies.objects.get(name=data['company']),
        applicant = cmp.objects.get(username=data['applicant']),
        surname = data['surname'],
        first_name = data['first_name'],
        email = data['email']
    )
    modele_instance.save()
    return Response(data)
