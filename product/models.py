from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product/images/',blank=True,null=True)
    count = models.IntegerField(default=5)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name},{self.price},{self.description},{self.image},{self.count},{self.createdat},{self.updatedat}"