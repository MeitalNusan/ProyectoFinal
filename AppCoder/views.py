from django.shortcuts import render
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
    return render(request, 'AppCoder/inicio.html')

def registrarse(request):
    return render(request, 'AppCoder/registrarse.html')

#def login(request):
 #   return render(request, 'AppCoder/perfil.html')

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
                return render(request,"AppCoder/inicio.html", {'usuario': usuario, 'mensaje': "Bienvenido al sistema"})

            else:
                return render(request, "AppCoder/login.html", {'mensaje': 'usuario incorrecto, vuelva a logearse'})
        else:
            return render(request, "AppCoder/inicio.html",{'mensaje': 'Error, formulario invalido, vuelva a logearse'})
    else:
        form=AuthenticationForm()
        return render(request,"AppCoder/login.html", {'form': form})

def registerarse(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request,"AppCoder/inicio.html", {'mensaje': f"usuario {username} creado"})
        else:
            return render(request, "AppCoder/inicio.html",{'mensaje':'formulario incorrecto'})

    else:
        form = UserRegistrationForm()
        return render(request, "AppCoder/registrarse.html", {'form':form})
   

