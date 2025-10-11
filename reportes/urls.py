from django.urls import path
from . import views

urlpatterns = [
    path('', views.reportes, name='reportes'),
    path('exportar_excel/', views.exportar_excel, name='exportar_excel'),
    path('exportar_excel_completo/', views.exportar_excel_completo, name='exportar_excel_completo'),
    path('exportar_pdf/', views.exportar_pdf, name='exportar_pdf'),
    path('exportar_pdf_completo/', views.exportar_pdf_completo, name='exportar_pdf_completo'),
]
