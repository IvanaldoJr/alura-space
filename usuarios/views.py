from django.shortcuts import render

from usuarios.forms import loginForms

def login(request):
    form = loginForms()
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    return render(request, "usuarios/cadastro.html")