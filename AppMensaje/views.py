from django.shortcuts import render
from .models import *
from AppMensaje.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required





def inicio(request):
    return render(request, "AppMensaje/inicio.html")
  
class MensajeCreacion(LoginRequiredMixin,CreateView):
    model = Mensajes
    success_url=reverse_lazy('mensajes')
    fields=['emisor', 'receptor','cuerpo']

def agregarMensaje(request):
    user=User.objects.get(username=request.user)
    if request.method == 'POST':
        formulario=AuthenticationForm(request=request, data=request.POST)
        formulario=MensajeForm(request.POST, request.FILES)
        if formulario.is_valid():        
            mensaje=Mensajes(user=user, avatar=formulario.cleaned_data['avatar'])
            mensaje.save()
            return render(request, 'AppMensaje/mensajes.html', {'usuario':user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE'})
    else:
        formulario=MensajeForm()
    return render(request, 'AppMensaje/agregarMensaje.html', {'form':formulario, 'usuario':user})