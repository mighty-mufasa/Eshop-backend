from rest_framework import views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import *

@api_view(['GET'])
def Hello(request):
    return Response({'msg': 'Hello World!'})

# show any data that user sends
@api_view(['GET','POST'])
def acceptData(request):
    print(request.method)
    print(request.data)
    return Response({'msg':'Accept Data', 'data': request.data})
