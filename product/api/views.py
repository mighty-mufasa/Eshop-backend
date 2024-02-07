from rest_framework import views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import *
from category.models import *
from .serialize import *
from rest_framework.generics import ListAPIView

class allProductsGeneric(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.productsList()

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

@api_view(['GET'])
def getProduct(request,id):
    product=Product.productDetails(id)
    dataJSON=ProductSerializer(product).data
    return Response({'model':'Product', 'Product':dataJSON})    

@api_view(['POST'])
def addProduct(request):
    print("==========>", request.POST)
    obj=ProductSerializer(data=request.data)
    if (obj.is_valid()):
        print("==========> Hello World1111111")
        # Product.productAddAPI(request)
        obj.save()
        return Response({'msg':'Product added successfully'})
    print("==========> Hello World")
    return Response({'msg':'Product not added', 'error':obj.errors})

@api_view(['PUT'])
def updateProduct(request,id):
    updateProduct=Product.objects.filter(id=id)
    if updateProduct:
        serializedProduct= ProductSerializer(instance=updateProduct,data=request.data)
        print("outer",serializedProduct)
        if (serializedProduct.is_valid()):
            print("inner")
            serializedProduct.save()
            return Response({'msg':'Product Updated successfully', "product":serializedProduct})
        else:
            return Response({'msg':'Product Not Valid'})
    return Response({'msg':'Product not found'})

@api_view(['DELETE'])
def deleteProduct(request,id):
    deletedProduct=Product.objects.filter(id=id).first()
    if deletedProduct:
        Product.objects.filter(id=id).delete()
        return Response({'msg':'Product Deleted successfully'})
    return Response({'msg':'Product not found'})