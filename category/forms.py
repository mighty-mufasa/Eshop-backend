from django import forms
from .models import Category
from django.core.exceptions import ValidationError

class CategoryForm(forms.Form):
    name = forms.CharField(min_length=3,max_length=25,required=True)
    email = forms.EmailField(required=True)
    image = forms.ImageField()
    age = forms.IntegerField(required=True,initial=22)

    # add constraint for name (unique)
    def clean_name(self):
        userEnteredName = self.cleaned_data['name']
        obj = Category.objects.filter(name=userEnteredName).exists()
        if obj:
            print(f"Category name {userEnteredName} already exist before and name is unique.")
            raise ValidationError("Category name must be unique")
        else:
            return True

    # add constraint for email (unique)
    def clean_email(self):
        userEnteredEmail = self.cleaned_data['email']
        obj = Category.objects.filter(email=userEnteredEmail).exists()
        if obj:
            print(f"Category email {userEnteredEmail} already exist before and email is unique.")
            raise ValidationError("Category email must be unique")
        else:
            return True