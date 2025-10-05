from django.shortcuts import render

def perfil(request):
    return render(request, "usuarios/perfil.html")
