from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def registrarse(request):
    return render(request, 'AppCoder/registrarse.html')

def login(request):
    return render(request, 'AppCoder/login.html')

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

