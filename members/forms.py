from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
        'class':'form-control'
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password',
        'class':'form-control'
    }))
    email=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Email',
        'class':'form-control',
    }))
    username=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Username',
        'class':'form-control',
    }))
    class Meta:
        model = User
        fields= ['username','email','password1','password2']