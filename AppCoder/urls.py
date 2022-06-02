from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', inicio, name="inicio"),
   
    path('registrarse/', registrarse, name="registrarse"),
    path('logout/', logout, name= "logout"),
    path('login/', login_request, name= "login"),
   
    path('facebook/', facebook, name="facebook"),
    path('instagram/', instagram, name="instagram"),
    path('twitter/', twitter, name="twitter"),
    path('sobre/', sobre, name="sobre"),

    path('perfil/nuevo/', PerfilCreacion.as_view(), name='perfil'),
  
    
    
]
