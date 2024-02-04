from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(min_length=3, required=True)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    description = forms.CharField(max_length=250)
    image = forms.ImageField()
    count = forms.IntegerField(required=True)