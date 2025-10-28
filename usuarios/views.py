from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#@login_required
def perfil(request):
    user = request.user

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        mensaje = request.POST.get("mensaje")

        # Actualiza los datos del usuario (solo el nombre por ahora)
        user.first_name = nombre
        user.save()

        messages.success(request, "✅ Cambios guardados correctamente.")
        return redirect("perfil")

    context = {
        "nombre": user.first_name or user.username,
        "mensaje": "Bienvenido a tu perfil. Aquí puedes gestionar tu cuenta.",
    }

    return render(request, "usuarios/perfil.html", context)
