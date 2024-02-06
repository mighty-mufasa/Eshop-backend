from django.shortcuts import render,reverse,redirect
from django.contrib.auth import authenticate

# Create your views here.
def Myprofile(request):
    return redirect('/')