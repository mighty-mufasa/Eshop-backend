from django.urls import path,include
from .views import *

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('profile/',Myprofile,name="myprofile"),
]