from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', inicio, name="inicio"),
    path('facebook/', facebook, name="facebook"),
    path('instagram/', instagram, name="instagram"),
    path('twitter/', twitter, name="twitter"),
    path('sobre/', sobre, name="sobre"),
    path('perfil/', perfil, name="perfil"),

    path('perfil/nuevo/', PerfilCreacion.as_view(), name='perfil_crear'),
    path('perfil/list', PerfilList.as_view(), name='perfil_listar'),
    path('perfil/<pk>', PerfilDetalle.as_view(), name='perfil_detalle'),
    path('perfil/editar/<pk>', PerfilEdicion.as_view(), name='perfil_editar'),
    path('perfil/borrar/<pk>', PerfilEliminacion.as_view(), name='perfil_borrar'),
    path('posteo/nuevo/', PosteoCreacion.as_view(), name='posteo_crear'),


    path('login/', login_request, name= "login"),
    path('registrarse/', register, name="registrarse"),
    path('logout/', LogoutView.as_view(template_name="AppCoder/logout.html"), name= "logout"),
    path('editarPerfil/', editarPerfil, name= "editarPerfil"),
   


   
    path('agregarAvatar/', agregarAvatar, name= "agregarAvatar"),
    
    path('sobre2/', sobre2, name= "sobre2"),
    
    
   
    

]
