from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *



class UserRegistrationForm(UserCreationForm):
     email=forms.EmailField(required=True)
     password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
     password2= forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

     class Meta:
         model = User
         fields=('username','email','password1','password2')
         help_texts={campo:"" for campo in fields}

class UserEditForm(UserCreationForm):
    email=forms.EmailField(required="Modificar Mail")
    password1= forms.CharField(label="Modificar Contraseña ", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    last_name= forms.CharField(label="Modificar Apellido", widget=forms.PasswordInput)
    first_name= forms.CharField(label="Modificar Nombre", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields=('email','password1','password2','last_name','first_name')
        help_texts={campito:"" for campito in fields}

class AvatarForm(forms.Form):
    avatar=forms.ImageField(label="avatar")


class ImagenForm(forms.Form):
    imagen=forms.ImageField(label="imagenes")
    
