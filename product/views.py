from django.shortcuts import render
from django.http import  HttpResponse
from .models import *

def hello(request):
    return  render(request,'index.html')
    # return  HttpResponse('<h1>Hello Omara</h1>')

def productList(request):
    context={'products':Product.objects.all}
    return  render(request,'product/index.html',context)

def productdetails(request,productid):
    obj=Product.objects.get(id=productid)
    context={'product':obj}
    # context={'product':Product.objects.get(id=productid)}
    return  render(request,'product/details.html',context)

def aboutUs(request):
    return  render(request,'aboutUs.html')