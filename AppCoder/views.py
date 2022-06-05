from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from AppCoder.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def inicio(request):
    url="HOLA!"
    return render(request, "AppCoder/inicio.html", {"url":url})
  


def perfil(request):
    return render(request, 'AppCoder/perfil.html')


def facebook(request):
    respuesta="Todavia no existe una pagina de Facebook"
    return HttpResponse(respuesta)

def instagram(request):
    respuesta="Todavia no existe una pagina de Instagram"
    return HttpResponse(respuesta)

def twitter(request):
    respuesta="Todavia no existe una pagina de Twitter"
    return HttpResponse(respuesta)

def sobre(request):
    return render(request, 'AppCoder/sobre.html')

def sobre2(request):
    return render(request, "AppCoder/sobre2.html")   


#---------------------------------

class PerfilCreacion(LoginRequiredMixin,CreateView):
    model = Perfil
    success_url=reverse_lazy('posteo/nuevo')
    fields=['nombre','email', 'contraseña', 'linkDeInteres']

class PerfilList(LoginRequiredMixin,ListView):
    model = Perfil
    template_name=('AppCoder/perfil_list.html')

class PerfilDetalle(LoginRequiredMixin,DetailView):
    model = Perfil
    template_name=('AppCoder/perfil_detalle.html')

class PerfilEdicion(LoginRequiredMixin,UpdateView):
    model = Perfil
    success_url=reverse_lazy('perfil_list')
    fields=['nombre','email', 'contraseña', 'linkDeInteres']


class PerfilEliminacion(LoginRequiredMixin,DeleteView):
    model = Perfil
    success_url=reverse_lazy('perfil_list')
    fields=['nombre','email', 'contraseña', 'linkDeInteres']


class PosteoCreacion(LoginRequiredMixin, CreateView):
    model = Posteo
    success_url=reverse_lazy('perfil')
    fields=['nombre','titulo', 'fecha', 'descripcion']
#-------------------------------------------------------------------

def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            clave=form.cleaned_data.get('password')

            user=authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request,"AppCoder/posteoNuevo.html", {'usuario': usuario, 'mensaje': "Bienvenido a Nuevo Mundo"})

            else:
                return render(request, "AppCoder/inicio.html", {'mensaje': 'usuario incorrecto, intente ingresar nuevamente'})
        else:
            return render(request, "AppCoder/login.html",{'mensaje': 'Error, formulario invalido, vuelva a loguearse'})
    else:
        form=AuthenticationForm()
        return render(request,"AppCoder/login.html", {'formulario': form})

def registrarse(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request,"AppCoder/posteoNuevo.html", {'mensaje': f"usuario {username} creado"})
        else:
            return render(request, "AppCoder/inicio.html",{'mensaje':'formulario incorrecto'})

    else:
        form = UserRegistrationForm()
        return render(request, "AppCoder/registrarse.html", {'form':form})
    

#----------------------------------------------------------------------------
@login_required
def agregarAvatar(request):
    user=User.objects.get(username=request.user)
    if request.method == 'POST':
        formulario=AuthenticationForm(request=request, data=request.POST)
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.get(user=request.user)
            if(avatarViejo.avatar):
                avatarViejo.delete()
            avatar=Avatar(user=user, avatar=formulario.cleaned_data['avatar'])
            avatar.save()
            return render(request, 'AppCoder/perfil.html', {'usuario':user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE'})
    else:
        formulario=AvatarForm()
    return render(request, 'AppCoder/agregarAvatar.html', {'formulario2':formulario, 'usuario':user})

@login_required
def editarPerfil(request):
    usuario=request.user
    
    if request.method == "POST":
        formulario=UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()
            return render(request,"AppCoder/inicio.html", {'usuario': usuario, 'mensaje':'Usuario Modificado'})

    else:
        formulario=UserEditForm(instance=usuario)
    return render(request,"ApCoder/editarPerfil.html",{'formulario':formulario, 'usuario':usuario.username})

#--------------------------------------------------------------
def perfilNuevo(request):
    return render(request, "AppCoder/posteoNuevo")    

def posteoNuevo(request):
    return render(request, "AppCoder/posteoNuevo.html")


class MensajeCreacion(LoginRequiredMixin,CreateView):
    model = Mensajes
    success_url=reverse_lazy('posteo/nuevo')
    fields=['emisor', 'receptor']
    