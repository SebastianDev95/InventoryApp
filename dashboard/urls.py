
from django.urls import path
from . import views  # Importa tu archivo views.py

urlpatterns = [
    # --- Autenticación (Nombres ÚNICOS) ---
    
    # Ruta de Login (Tus plantillas usan 'login')
    path('login/', views.login_vista, name='login'),
    
    # Ruta de Registro (Tus plantillas usan 'register')
    path('register/', views.registro_vista, name='register'),
    
    # Ruta de Logout
    path('logout/', views.logout_vista, name='logout'),

    
    # --- Aplicación Principal ---
    
    path('dashboard/', views.Dashboard, name='dashboard'),

    
    # --- CRUD de Productos ---
    
    path('producto/nuevo/', views.nuevo_producto, name='nuevo_producto'),
    path('producto/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('producto/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/eliminar_seleccionados/', views.eliminar_productos_seleccionados, name='eliminar_productos_seleccionados'),
]