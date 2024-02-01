from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
products=[
    {'id':1,'Name':'os','path':'os.png'},
    {'id':2,'Name':'IOT','path':'iot.png'},
    {'id':3,'Name':'Python','path':'python.jpeg'},
    {'id':4,'Name':'php','path':'php.png'},
]

def hello(request):
    return  render(request,'index.html')
    # return  HttpResponse('<h1>Hello Omara</h1>')

def productList(request):
    context={}
    context['products']=products
    return  render(request,'product/index.html',context)

def productdetails(request,productid):
    product=filter(lambda t:t['id']==productid,products)
    product=list(product)
    context={}
    context['product']=product
    return  render(request,'product/details.html',context)
    # if product:
    #     # return HttpResponse(product)
    #     return  render(request,'product/index.html')
    # return HttpResponse('<span style="color:red">product not found</span>')

def aboutUs(request):
    return  render(request,'aboutUs.html')