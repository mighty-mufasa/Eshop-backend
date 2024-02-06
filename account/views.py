from django.shortcuts import render,reverse,redirect
from django.contrib.auth import authenticate
from django.views.generic import CreateView
# from  product.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class Registrationform(CreateView):
    model = User
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    context_object_name = 'form'
    success_url = reverse_lazy('login')

def Myprofile(request):
    return redirect('/')