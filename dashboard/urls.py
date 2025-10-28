from django.urls import path
from dashboard.views import *


urlpatterns=[
    path("dashboard",Dashboard,name="Dashboard"),
    path("Editarproducto", editar, name="editar"),
    path("Nuevoproducto", nuevo, name="editar")


]