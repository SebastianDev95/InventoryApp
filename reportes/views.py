from django.shortcuts import render
from django.http import HttpResponse

def reportes(request):
    return render (request,"reportes/reporte.html")

