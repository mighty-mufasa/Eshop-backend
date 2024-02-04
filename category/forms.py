from django import forms
from .models import Category
from django.core.exceptions import ValidationError

class CategoryForm(forms.Form):
    name = forms.CharField(min_length=3,max_length=25,required=True)
    email = forms.EmailField(required=True)
    image = forms.ImageField()
    age = forms.IntegerField(required=True,initial=22)

    # add constraint for email (unique)
    def clean_email(self):
        userEnteredEmail = self.cleaned_data['email']
        obj = Category.objects.filter(email=userEnteredEmail).exists()
        if obj:
            print(f"Category email {userEnteredEmail} already exist before and email is unique.")
            raise ValidationError("name must be unique")
        else:
            return True