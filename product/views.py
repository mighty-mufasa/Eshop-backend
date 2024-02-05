from django.shortcuts import render,reverse
from django.http import  HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *

def hello(request):
    return  render(request,'index.html')

def productUpdate(request,id):
    # product=Product.objects.get(id=id)
    product=Product.productDetails(id)
    context={'product':product}
    if request.method == 'POST':
            if (request.POST['pName'] != ''):
                Product.productUpdate(request,id)
                # Product.objects.filter(id=id).update(
                #                 name=request.POST['pName'],
                #                 price=request.POST['pPrice'],
                #                 description=request.POST['pDescription'],
                #                 count=request.POST['pCount']
                #                 )
                return HttpResponseRedirect(reverse('product.all'))
            else:
                context['msg']='Kindly fill all fields'
    context['categories']=Category.objects.all()
    return render(request,'product/update.html',context)
# if request.method == 'POST':
#         Product.productAdd(request)
#         # Product.objects.create(name=request.POST['pName'],
#         #                        price=request.POST['pPrice'],
#         #                        description=request.POST['pDescription'],
#         #                        image=request.FILES['pImage'],
#         #                        count=request.POST['pCount']
#         #                        )
#         return HttpResponseRedirect(reverse('product.all'))
#     context={'categories':Category.objects.all()}
#     return render(request,'product/add.html',context)

def productDelete(request,id):
    # Product.objects.filter(id=id).delete()
    Product.productDelete(id)
    return HttpResponseRedirect(reverse('product.all'))

def productAddForm(request):
    form = ProductForm()
    context = {'form': form}
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if (form.is_valid()):
            # Product.productAdd(request) ==>Must be handled first to be dynamic for gui and forms
            Product.objects.create(name=request.POST['name'],
                                price=request.POST['price'],
                                description=request.POST['description'],
                                image=request.FILES['image'],
                                count=request.POST['count'],
                                category=Category.objects.get(id=request.POST['category'])
                                
                                )
            return HttpResponseRedirect(reverse('product.all'))
        else:
            context['msg'] = 'Data not completed'
    return render(request,'product/addForm.html',context)

def addProduct(request):
    if request.method == 'POST':
        Product.productAdd(request)
        # Product.objects.create(name=request.POST['pName'],
        #                        price=request.POST['pPrice'],
        #                        description=request.POST['pDescription'],
        #                        image=request.FILES['pImage'],
        #                        count=request.POST['pCount']
        #                        )
        return HttpResponseRedirect(reverse('product.all'))
    context={'categories':Category.objects.all()}
    return render(request,'product/add.html',context)

def productList(request):
    # context={'products':Product.objects.all()}
    context={'products':Product.productsList()}
    return  render(request,'product/index.html',context)

def productdetails(request,productid):
    # obj=Product.objects.get(id=productid)
    obj=Product.productDetails(productid)
    context={'product':obj}
    # context={'product':Product.objects.get(id=productid)}
    return  render(request,'product/details.html',context)

def aboutUs(request):
    return  render(request,'aboutUs.html')