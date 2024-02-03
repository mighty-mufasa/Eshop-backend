from django.contrib import admin
from .models import Product
# Register your models here.

# to show product table in admin page
admin.site.register(Product)