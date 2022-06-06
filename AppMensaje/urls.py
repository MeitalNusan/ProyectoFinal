from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('mensaje/nuevo/', MensajeCreacion.as_view(), name='mensaje'),

    
    
    

]
