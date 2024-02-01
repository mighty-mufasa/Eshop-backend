from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
categories=[
    {'id':1,'Name':'os','path':'os.png'},
    {'id':2,'Name':'IOT','path':'iot.png'},
    {'id':3,'Name':'Python','path':'python.jpeg'},
    {'id':4,'Name':'php','path':'php.png'},
    {'id':5,'Name':'os','path':'os.png'},
    {'id':6,'Name':'IOT','path':'iot.png'},
    {'id':7,'Name':'Python','path':'python.jpeg'},
    {'id':8,'Name':'php','path':'php.png'},
]

def categoryList(request):
    context={}
    context['categories']=categories
    return  render(request,'category/index.html',context)

def categorydetails(request,categoryid):
    category=filter(lambda t:t['id']==categoryid,categories)
    category=list(category)
    context={}
    context['category']=category
    return  render(request,'category/details.html',context)
    