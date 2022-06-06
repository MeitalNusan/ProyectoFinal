from django.db import models
from django.forms import ImageField
from django.contrib.auth.models import User

class Posteos(models.Model):
    nombre=models.CharField(max_length=50)
    titulo=models.CharField(max_length=150)
    subtitulo=models.CharField(max_length=150)
    fecha=models.DateField()
    descripcion=models.TextField(max_length=150)
    avatar= models.ImageField(upload_to='avatar', blank=True, null=True)

    def __str__(self):
     return self.nombre + " " + self.titulo + " " + self.subtitulo + self.descripcion

class Perfiles(models.Model):
    nombre=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    contraseña=models.IntegerField()
    linkDeInteres=models.URLField(max_length=150)
    
    

    def __str__(self):
     return self.nombre + " " + self.email + self.linkDeInteres

class Blog(models.Model):
    nombre=models.CharField(max_length=50)
    url=models.URLField(max_length=150)

    def __str__(self):
        return self.nombre + " " + self.url

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    avatar= models.ImageField(upload_to='avatar', blank=True, null=True)

class Mensajes(models.Model):
    emisor:models.CharField(max_length=50)
    receptor:models.CharField(max_length=50)
    

