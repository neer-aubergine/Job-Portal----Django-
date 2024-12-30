from django import forms
from .models import Company
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name' , 'address' , 'contact']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username' , 'email' , 'password1' , 'password2')