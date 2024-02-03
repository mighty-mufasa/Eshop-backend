from django.urls import path
from . import  views
urlpatterns = [
    path('',views.categoryList,name="category.all"),
    path('<int:id>',views.categorydetails,name="category.details"),
]