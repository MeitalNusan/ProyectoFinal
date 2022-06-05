from django.db import models

class Mensajes(models.Model):
    emisor:models.CharField(max_length=50)
    receptor:models.CharField(max_length=50)
    
