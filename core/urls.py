from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("banner.urls")),
    path("Dashboard",include("dashboard.urls")),
    path("Reportes",include("reportes.urls")),
    path("Usuarios",include("usuarios.urls"))
]
