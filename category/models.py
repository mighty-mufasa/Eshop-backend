from django.db import models
from django.utils.timezone import now

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='category/images/',blank=True,null=True)
    age = models.IntegerField(default=22)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.name},{self.email},{self.image},{self.age},{self.createdat},{self.updatedat}"
    
    @classmethod
    def categoryAdd(self,request):
        print("request========================>",request.POST)
        return self.objects.create(name=request.POST['cName'],
                                   email=request.POST['cEmail'],
                                   image=request.POST['cImage'],
                                   age=request.POST['cAge'],
                                   )
    @classmethod
    def categoryUpdate(self,request,id):
        return self.objects.filter(id=id).update(
                                name=request.POST['cName'],
                                email=request.POST['cEmail'],
                                image=request.POST['cImage'],
                                age=request.POST['cAge'],
                                )

    @classmethod
    def categoryList(self):
        return self.objects.all()

    @classmethod
    def categoryDetails(cls,id):
        return cls.objects.get(id=id)

    @classmethod
    def categoryDelete(self,id):
        return self.objects.filter(id=id).delete()

    # Instance methods
    def getImgURL(self): 
        return f"/media/{self.image}"