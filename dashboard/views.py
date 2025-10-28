from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages


def Dashboard(request):
    return render(request, "dashboard/home.html")

def editar(request):
    return render(request,"dashboard/editar.html")

def nuevo(request):
    return render(request,"dashboard/nuevo.html")

def logout_vista(request):

    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('login')
