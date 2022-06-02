from django.db import models
from django.forms import ImageField
from django.contrib.auth.models import User

class Posteo(models.Model):
    nombre=models.CharField(max_length=50)
    titulo=models.CharField(max_length=150)
    subtitulo=models.CharField(max_length=150)
    fecha=models.DateField()
    avatar=ImageField()

    def __str__(self):
     return self.nombre + " " + self.titulo + " " + self.subtitulo 

class Perfil(models.Model):
    nombre=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    contraseña=models.IntegerField()
    link=models.SlugField(max_length=150)
    descripcion=models.CharField(max_length=150)
    

    def __str__(self):
     return self.nombre + " " + self.email + " " + self.descripcion

class Blog(models.Model):
    nombre=models.CharField(max_length=50)
    url=models.SlugField(max_length=150)

    def __str__(self):
        return self.nombre + " " + self.url
