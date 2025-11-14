from django.urls import path
from . import views

urlpatterns = [
    path("perfil/", views.perfil, name="perfil"),
    path('eliminar-cuenta/', views.eliminar_cuenta, name='eliminar_cuenta'),
]
