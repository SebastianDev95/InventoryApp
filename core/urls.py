from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("banner.urls")),
    path("",include("dashboard.urls")),
    path("",include("reportes.urls")),
    path("",include("usuarios.urls")),
]
