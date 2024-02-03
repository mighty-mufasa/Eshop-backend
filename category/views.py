from django.shortcuts import render
from django.http import  HttpResponse
from .models import *

# Create your views here.

def categoryList(request):
    context={'categories':Category.objects.all()}
    return render(request,'category/index.html',context)

def categorydetails(request,id):
    obj=Category.objects.get(id=id)
    context={'category':obj}
    # context={'category':Category.objects.get(id=id)}
    return  render(request,'category/details.html',context)