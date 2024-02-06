from rest_framework import views
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def Hello(request):
    return Response({'msg': 'Hello World!'})