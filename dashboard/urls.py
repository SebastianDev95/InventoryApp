from django.urls import path
from dashboard.views import *

urlpatterns = [
    path("", Dashboard, name="Dashboard"),  
    path("editarproducto/", editar, name="editar"),  
    path("nuevoproducto/", nuevo, name="nuevo"),     
]
