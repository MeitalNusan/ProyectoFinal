from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name="inicio"),
    path('login/', login, name="login"),
    path('registrarse/', registrarse, name="registrarse"),
    path('logout/', logout, name= "logout"),
   
    path('facebook/', facebook, name="facebook"),
    path('instagram/', instagram, name="instagram"),
    path('twitter/', twitter, name="twitter"),
    path('sobre/', sobre, name="sobre"),
  
    
    
]
