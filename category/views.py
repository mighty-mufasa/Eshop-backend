from django.shortcuts import render,reverse
from django.http import  HttpResponseRedirect
from .models import *

# Create your views here.

def categoryOldData(request,id):
    obj=Category.objects.get(id=id)
    context={'obj':obj}
    return render(request,'category/update.html',context)

def categoryUpdate(request,id):
    if request.method == 'POST':
        obj=Category.objects.get(id=id)
        obj.name=request.POST['cName']
        obj.email=request.POST['cEmail']
        obj.image=request.POST['cImage']
        obj.age=request.POST['cAge']
        obj.save()

        return HttpResponseRedirect(reverse('category.all'))
    
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