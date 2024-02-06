from django.urls import path
from .views import *

urlpatterns = [
    path('Hello/',Hello,name='hello'),
    path('acceptData/',acceptData,name='acceptData'),
]