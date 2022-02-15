from dataclasses import field
from tkinter import Widget
from turtle import width
from .models import *
from django import forms
from django.forms import ModelForm , TextInput, PasswordInput,Textarea 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
            
class CreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name','text']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class':'form-control'}),
        }

class CreateArt(ModelForm):
    class Meta:
        model = Article
        fields = ['text_article']
        widgets = {
            'text_article': forms.TextInput(attrs={'class':'form-control'}),
        }

            
             