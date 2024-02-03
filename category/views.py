from django.shortcuts import render,reverse
from django.http import  HttpResponseRedirect
from .models import *

# Create your views here.

def categoryDelete(request,id):
    Category.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('category.all'))

def addCategory(request):
    if request.method == 'POST':
        Category.objects.create(name=request.POST['cName'],
                                email=request.POST['cEmail'],
                                image=request.POST['cImage'],
                                age=request.POST['cAge']
                               )
        return HttpResponseRedirect(reverse('category.all'))
    return render(request,'category/add.html')

def categoryList(request):
    context={'categories':Category.objects.all()}
    return render(request,'category/index.html',context)

def categorydetails(request,id):
    obj=Category.objects.get(id=id)
    context={'category':obj}
    # context={'category':Category.objects.get(id=id)}
    return  render(request,'category/details.html',context)