from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from AppCoder.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def inicio(request):
     avatar=Avatar.objects.filter(user=request.user)
     return render(request, 'AppCoder/inicio.html', {"url":avatar[0].avatar.url})
  


def perfil(request):
    return render(request, 'AppCoder/perfil.html')

def logout(request):
    return render(request, 'AppCoder/logout.html')



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


#---------------------------------


def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            clave=form.cleaned_data.get('password')

            user=authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request,"AppCoder/perfil.html", {'usuario': usuario, 'mensaje': "Bienvenido al sistema"})

            else:
                return render(request, "AppCoder/login.html", {'mensaje': 'usuario incorrecto, vuelva a logearse'})
        else:
            return render(request, "AppCoder/inicio.html",{'mensaje': 'Error, formulario invalido, vuelva a logearse'})
    else:
        form=AuthenticationForm()
        return render(request,"AppCoder/login.html", {'form': form})

def registrarse(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request,"AppCoder/perfil.html", {'mensaje': f"usuario {username} creado"})
        else:
            return render(request, "AppCoder/inicio.html",{'mensaje':'formulario incorrecto'})

    else:
        form = UserRegistrationForm()
        return render(request, "AppCoder/registrarse.html", {'form':form})

class PerfilCreacion(CreateView):
    model = Perfil
    success_url=reverse_lazy('perfil_crear')
    fields=['nombre','email', 'contraseña', 'linkDeInteres']

class PerfilList(ListView):
    model = Perfil
    template_name=('AppCoder/perfil_list.html')

class PerfilDetalle(DetailView):
    model = Perfil
    template_name=('AppCoder/perfil_detalle.html')

class PerfilEdicion(UpdateView):
    model = Perfil
    success_url=reverse_lazy('perfil_list')
    fields=['nombre','email', 'contraseña', 'linkDeInteres']


class PerfilEliminacion(DeleteView):
    model = Perfil
    success_url=reverse_lazy('perfil_list')
    fields=['nombre','email', 'contraseña', 'linkDeInteres']



def perfilNuevo(request):
    return render(request, "AppCoder/posteoNuevo")

class PosteoCreacion(CreateView):
    model = Posteo
    success_url=reverse_lazy('perfil')
    fields=['nombre','titulo', 'fecha', 'descripcion']


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

    
def sobre2(request):
    return render(request, "AppCoder/sobre2.html")

def posteoNuevo(request):
    return render(request, "AppCoder/posteoNuevo.html")

    