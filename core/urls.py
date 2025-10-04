from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("banner.urls")), 
    path("perfil/", include("usuarios.urls")),
]
