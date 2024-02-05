from django import forms
from .models import *

class ProductFormModel(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ['name', 'price', 'description', 'image', 'count', 'category']
        fields = '__all__'
        exclude = ['createdat' , 'updatedat']
        

