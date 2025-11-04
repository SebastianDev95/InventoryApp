
from django.urls import path
from . import views  # Importa tu archivo views.py

urlpatterns = [
    path('login/', views.login_vista, name='login'),
    path('register/', views.registro_vista, name='register'),
    path('logout/', views.logout_vista, name='logout'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('producto/nuevo/', views.nuevo_producto, name='nuevo_producto'),
    path('producto/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('producto/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/eliminar_seleccionados/', views.eliminar_productos_seleccionados, name='eliminar_productos_seleccionados'),
    path('reportes/', views.Dashboard, name='reportes'),
    path('perfil/', views.Dashboard, name='perfil'),
]