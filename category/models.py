from django.db import models
from django.utils.timezone import now

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.CharField(max_length=200,null=True)
    age = models.IntegerField(default=22)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.name},{self.email},{self.image},{self.age},{self.createdat},{self.updatedat}"