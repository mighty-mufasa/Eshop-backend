from django.shortcuts import render,reverse
from django.http import  HttpResponseRedirect, HttpResponse
from .models import *

def hello(request):
    return  render(request,'index.html')

def productUpdate(request,id):
    product=Product.objects.get(id=id)
    context={'product':product}
    if request.method == 'POST':
            if (request.POST['pName'] != ''):
                Product.objects.filter(id=id).update(
                                name=request.POST['pName'],
                                price=request.POST['pPrice'],
                                description=request.POST['pDescription'],
                                count=request.POST['pCount']
                                )
                return HttpResponseRedirect(reverse('product.all'))
            else:
                context['msg']='Kindly fill all fields'
    return render(request,'product/update.html',context)

def productDelete(request,id):
    Product.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('product.all'))

def addProduct(request):
    if request.method == 'POST':
        Product.objects.create(name=request.POST['pName'],
                               price=request.POST['pPrice'],
                               description=request.POST['pDescription'],
                               image=request.FILES['pImage'],
                               count=request.POST['pCount']
                               )
        return HttpResponseRedirect(reverse('product.all'))
    return render(request,'product/add.html')

def productList(request):
    context={'products':Product.objects.all()}
    return  render(request,'product/index.html',context)

def productdetails(request,productid):
    obj=Product.objects.get(id=productid)
    context={'product':obj}
    # context={'product':Product.objects.get(id=productid)}
    return  render(request,'product/details.html',context)

def aboutUs(request):
    return  render(request,'aboutUs.html')