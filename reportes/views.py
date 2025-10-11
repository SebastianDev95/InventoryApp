from django.shortcuts import render
from django.http import HttpResponse
import openpyxl
from openpyxl.styles import Font, Alignment
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

def reportes(request):
    return render(request, "reportes/reporte.html")

# =============================
#   EXPORTAR A EXCEL (RESUMEN)
# =============================
def exportar_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Reporte Inventario"

    # Encabezado
    ws["A1"] = "Producto"
    ws["B1"] = "Categoría"
    ws["C1"] = "Stock"
    ws["D1"] = "Precio"
    for cell in ws["1:1"]:
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal="center")

    # Datos de ejemplo
    data = [
        ["Mouse", "Accesorios", 5, 25000],
        ["Teclado M", "Accesorios", 0, 40000],
        ["Monitor", "Accesorios", 8, 300000],
    ]
    for row in data:
        ws.append(row)

    # Enviar como respuesta
    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = 'attachment; filename="Reporte_Inventario.xlsx"'
    wb.save(response)
    return response


# =============================
#   EXPORTAR A EXCEL (COMPLETO)
# =============================
def exportar_excel_completo(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Inventario Completo"

    ws.append(["ID", "Producto", "Categoría", "Stock", "Precio", "Proveedor", "Fecha Ingreso"])
    for cell in ws["1:1"]:
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal="center")

    # Datos simulados
    data = [
        [1, "Mouse", "Accesorios", 5, 25000, "TechStore", "2024-01-10"],
        [2, "Teclado M", "Accesorios", 0, 40000, "PeriTech", "2024-02-15"],
        [3, "Monitor", "Accesorios", 8, 300000, "VisualCorp", "2024-03-02"],
        [4, "Laptop X", "Electrónicos", 12, 2500000, "TechStore", "2024-04-11"],
        [5, "Silla ergonómica", "Mobiliario", 7, 450000, "OfficePro", "2024-05-30"],
    ]
    for row in data:
        ws.append(row)

    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = 'attachment; filename="Inventario_Completo.xlsx"'
    wb.save(response)
    return response


# =============================
#   EXPORTAR A PDF (RESUMEN)
# =============================
def exportar_pdf(request):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setTitle("Reporte Inventario")

    pdf.drawString(100, 750, "Reporte de Inventario")
    pdf.line(100, 747, 500, 747)

    pdf.drawString(100, 720, "Mouse - Accesorios - 5 unidades - $25.000")
    pdf.drawString(100, 700, "Teclado M - Accesorios - 0 unidades - $40.000")
    pdf.drawString(100, 680, "Monitor - Accesorios - 8 unidades - $300.000")

    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')


# =============================
#   EXPORTAR A PDF (COMPLETO)
# =============================
def exportar_pdf_completo(request):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setTitle("Inventario Completo")

    pdf.drawString(100, 750, "Inventario Completo - Detalle de Productos")
    pdf.line(100, 747, 500, 747)

    y = 720
    data = [
        "Mouse - Accesorios - 5 unidades - $25.000 - TechStore",
        "Teclado M - Accesorios - 0 unidades - $40.000 - PeriTech",
        "Monitor - Accesorios - 8 unidades - $300.000 - VisualCorp",
        "Laptop X - Electrónicos - 12 unidades - $2.500.000 - TechStore",
        "Silla ergonómica - Mobiliario - 7 unidades - $450.000 - OfficePro",
    ]
    for line in data:
        pdf.drawString(100, y, line)
        y -= 20

    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')
