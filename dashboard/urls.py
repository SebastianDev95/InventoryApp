from django.urls import path
from dashboard.views import *

urlpatterns = [
    path("dashboard", Dashboard, name="dashboard"),  
    path("editarproducto/", editar, name="editar"),  
    path("nuevoproducto/", nuevo, name="nuevo"),
    path("logout", logout_vista, name="logout")

]