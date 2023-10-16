from rest_framework.response import Response
from rest_framework.decorators import api_view
from Adverts.models import Annonce
from Api.serializers import AnnonceSerializer

@api_view(['GET'])
def GetData(request):
    annonces = Annonce.objects.all()
    serializer = AnnonceSerializer(annonces, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def AddData(request):
    serializer = AnnonceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
