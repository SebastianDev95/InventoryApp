from django.shortcuts import render

def index(request):
    return render(request, "banner/index.html")

def register(request):
    return render(request,"banner/register.html")

def login(request):
    return render(request, "banner/login.html")
