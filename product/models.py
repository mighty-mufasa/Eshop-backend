from django.db import models
from category.models import *

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product/images/',blank=True,null=True)
    count = models.IntegerField(default=5)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    # object of Category model
    category = models.ForeignKey(Category,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name},{self.price},{self.description},{self.image},{self.count},{self.createdat},{self.updatedat}"
    
    @classmethod
    def productAdd(self,request):
        return self.objects.create(name=request.POST['pName'],
                                   price=request.POST['pPrice'],
                                   description=request.POST['pDescription'],
                                   image=request.FILES['pImage'],
                                   count=request.POST['pCount'],
                                   category=Category.objects.get(id=request.POST['pCategory'])
                                   )
    @classmethod
    def productUpdate(self,request,id):
        return self.objects.filter(id=id).update(
                                name=request.POST['pName'],
                                price=request.POST['pPrice'],
                                description=request.POST['pDescription'],
                                count=request.POST['pCount']
                                )
        
    @classmethod
    def productsList(self):
        return self.objects.all()
    
    @classmethod
    def productDetails(cls,id):
        return cls.objects.get(id=id)
    
    @classmethod
    def productDelete(self,id):
        return self.objects.filter(id=id).delete()
            
    # Instance methods
    def getImgURL(self): 
        return f"/media/{self.image}"