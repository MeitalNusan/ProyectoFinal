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
    return render(request, 'AppCoder/inicio.html',)
  


def perfil(request):
    imagen=Posteos.objects.all()
    return render(request, 'AppCoder/inicio.html', {'formulario':imagen})


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
    model = Perfiles
    success_url=reverse_lazy('perfil_listar')
    fields=['nombre','email', 'contraseña', 'linkDeInteres']

class PerfilList(LoginRequiredMixin,ListView):
    model = Perfiles
    template_name=('AppCoder/perfil_list.html')

class PerfilDetalle(LoginRequiredMixin,DetailView):
    model = Perfiles
    template_name=('AppCoder/perfil_detalle.html')

class PerfilEdicion(LoginRequiredMixin,UpdateView):
    model = Perfiles
    success_url=reverse_lazy('perfil_listar')
    fields=['nombre','email', 'contraseña', 'linkDeInteres']


class PerfilEliminacion(LoginRequiredMixin,DeleteView):
    model = Perfiles
    success_url=reverse_lazy('perfil_listar')
    fields=['nombre','email', 'contraseña', 'linkDeInteres']


class PosteoCreacion(LoginRequiredMixin, CreateView):
    model = Posteos
    success_url=reverse_lazy('perfil')
    fields=['user','nombre','titulo', 'fecha', 'descripcion','imagen']


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
                return render(request,"AppCoder/inicio.html", {'usuario': usuario, 'mensaje': "Bienvenido a Nuevo Mundo"})

            else:
                return render(request, "AppCoder/inicio.html", {'mensaje': 'usuario incorrecto, intente ingresar nuevamente'})
        else:
                return render(request, "AppCoder/login.html",{'mensaje': 'Error, formulario invalido, vuelva a loguearse'})
    else:
        form=AuthenticationForm()
    return render(request,"AppCoder/login.html", {'formulario': form})
           
           

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request,"AppCoder/inicio.html", {'mensaje': f"usuario {username} creado"})
        else:
        
            return render(request, "AppCoder/register.html", {'form':form})
    else:
        form = UserRegistrationForm()
    return render(request, "AppCoder/register.html", {'form':form})
    

#----------------------------------------------------------------------------
@login_required
def agregarAvatar(request):
    user=User.objects.get(username=request.user)
    if request.method == 'POST':
        formulario=AuthenticationForm(request=request, data=request.POST)
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if(len(avatarViejo)!=0):
                avatarViejo[0].delete()
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
    return render(request,"AppCoder/editarPerfil.html",{'formulario':formulario, 'usuario':usuario.username})

#--------------------------------------------------------------

