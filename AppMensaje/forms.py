from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MensajeForm(forms.Form):
    mensaje=forms.CharField(max_length=150)
    receptor:forms.CharField(max_length=50)
    cuerpo:forms.CharField(max_length=50)
    