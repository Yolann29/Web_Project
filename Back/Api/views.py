from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def GetData(request):
    person = {'name':'denis', 'age':28}
    return Response(person)