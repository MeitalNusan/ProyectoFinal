from django.db import models
from django.forms import CharField, ImageField
from django.contrib.auth.models import User

class Mensajes(models.Model):
    emisor:models.ForeignKey(User, on_delete=models.CASCADE)
    receptor:models.CharField(max_length=50)
    cuerpo:models.CharField(max_length=50)
    
