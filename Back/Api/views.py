from rest_framework.response import Response
from rest_framework.decorators import api_view
from utilisateur.models import advertisement, JobApplication, companies, cmp
from Api.serializers import AnnonceSerializer, CompaniesSerializer
import json

@api_view(['GET'])
def GetAnn(request):
    annonces = advertisement.objects.all()
    serializer = AnnonceSerializer(annonces, many=True)
    print(serializer.data)
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

print("lapin")