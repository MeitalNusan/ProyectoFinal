from django.db import models
from django.forms import ImageField
from django.contrib.auth.models import User

class Perfil(models.Model):
    nombre=models.CharField(max_length=50)
    titulo=models.CharField(max_length=150)
    subtitulo=models.CharField(max_length=150)
    fecha=models.DateField()
    avatar=ImageField()

