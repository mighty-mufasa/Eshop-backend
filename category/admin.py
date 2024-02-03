from django.contrib import admin
from .models import Category
# Register your models here.

# to show category table in admin page
admin.site.register(Category)