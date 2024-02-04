from django import forms
from .models import Product
from django.core.exceptions import ValidationError

class ProductForm(forms.Form):
    name = forms.CharField(min_length=3, required=True)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    description = forms.CharField(max_length=250)
    image = forms.ImageField()
    count = forms.IntegerField(required=True)

    # add constraint for name (unique)
    def clean_name(self):
        userEnteredName = self.cleaned_data['name']
        obj = Product.objects.filter(name=userEnteredName).exists()
        if obj:
            print(f"Product name {userEnteredName} already exist before and name is unique.")
            raise ValidationError("name must be unique")
        else:
            return True
