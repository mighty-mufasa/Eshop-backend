from django import forms

class CategoryForm(forms.Form):
    name = forms.CharField(min_length=3,max_length=25,required=True)
    email = forms.EmailField(required=True)
    image = forms.ImageField()
    age = forms.IntegerField(required=True,initial=22)