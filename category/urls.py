from django.urls import path
from . import  views
urlpatterns = [
    path('',views.categoryList),
    path('<int:categoryid>',views.categorydetails,name="categoryDetails"),
]