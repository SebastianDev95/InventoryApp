from django.shortcuts import render

def Dashboard(request):
    return render(request, "dashboard/home.html")

def editar(request):
    return render(request,"dashboard/editar.html")

def nuevo(request):
    return render(request,"dashboard/nuevo.html")
