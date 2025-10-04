from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("Banner", include("banner.urls")),
    path("dashboard", include("dashboard.urls")),
    path("usuarios", include("usuarios.urls")), 
    path("reportes", include("reportes.urls")),    
]
