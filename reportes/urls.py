# En reportes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL de la página de reportes
    path("reportes/", views.reportes, name="reportes"),

    # --- URLs de Exportación (Nuevas) ---
    path("exportar/excel/", views.exportar_excel, name="exportar_excel"),
    path("exportar/pdf/", views.exportar_pdf, name="exportar_pdf"),
    
    path("exportar/excel-completo/", 
         views.exportar_excel_completo, 
         name="exportar_excel_completo"),
         
    path("exportar/pdf-completo/", 
         views.exportar_pdf_completo, 
         name="exportar_pdf_completo"),
]