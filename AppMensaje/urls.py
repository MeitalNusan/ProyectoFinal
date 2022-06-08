from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('mensajes', MensajeCreacion.as_view(), name='mensaje'),
    path('mensaje/nuevo/', agregarMensaje, name='mensaje'),

    
    
    

]
