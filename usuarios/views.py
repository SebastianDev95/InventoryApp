from django.shortcuts import render


def Usuarios(request):
    return render(request, "usuarios/Users.html")
