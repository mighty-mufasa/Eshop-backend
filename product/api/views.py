from rest_framework import views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import *
from category.models import *
from .serialize import *


@api_view(['GET'])
def Hello(request):
    return Response({'msg': 'Hello World!'})

# show any data that user sends
@api_view(['GET','POST'])
def acceptData(request):
    print(request.method)
    print(request.data)
    return Response({'msg':'Accept Data', 'data': request.data})

# show all products in DB
# @api_view(['GET'])
# def allProducts(request):
#     products=Product.productsList()
#     print (products)
#     dataJSON=[]
#     for product in products:
#         dataJSON.append({"id": product.id, "name": product.name,"price":product.price ,
#                          "description": product.description, "count": product.count,
#                          "createdat": product.createdat, "updatedat": product.updatedat})
    
#     return Response({'model':'Product', 'Products':dataJSON})
    
@api_view(['GET'])
def allProducts(request):
    products=Product.productsList()
    dataJSON=ProductSerializer(products,many=True).data
    return Response({'model':'Product', 'Products':dataJSON})
    