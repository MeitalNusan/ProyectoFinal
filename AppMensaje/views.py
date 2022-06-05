from django.shortcuts import render
from .models import *
from AppCoder.forms import *
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
    success_url=reverse_lazy('posteo/nuevo')
    fields=['emisor', 'receptor']
