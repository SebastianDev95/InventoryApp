from django.contrib import admin
from django.urls import path, include
from usuarios.views import *



urlpatterns = [

    path("", Usuarios, name="Usuarios")

]