from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
import os

@login_required
def eliminar_cuenta(request):
    user = request.user
    user.delete()
    messages.success(request, "Tu cuenta ha sido eliminada correctamente.")
    return redirect('login')


@login_required
def perfil(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":

        # ELIMINAR CUENTA
        if "delete_account" in request.POST:
            return redirect("eliminar_cuenta")

        # Campos del formulario
        nombre = request.POST.get("nombre")
        mensaje = request.POST.get("mensaje")
        genero = request.POST.get("genero")
        hora = request.POST.get("hora")
        pais = request.POST.get("pais")
        zona = request.POST.get("zona")

        # --- Manejo del avatar ---
        if "delete_avatar" in request.POST:
            if profile.avatar and os.path.exists(profile.avatar.path):
                os.remove(profile.avatar.path)
            profile.avatar = None

        elif "avatar" in request.FILES:
            profile.avatar = request.FILES["avatar"]

        # --- Guardar datos ---
        user.first_name = nombre
        user.save()

        profile.mensaje = mensaje
        profile.genero = genero
        profile.hora = hora
        profile.pais = pais
        profile.zona = zona
        profile.save()

        messages.success(request, "Cambios guardados correctamente.")
        return redirect("perfil")

    context = {
        "nombre": user.first_name or user.username,
        "mensaje": profile.mensaje,
        "genero": profile.genero,
        "hora": profile.hora,
        "pais": profile.pais,
        "zona": profile.zona,
        "avatar_url": profile.avatar_url,
    }

    return render(request, "usuarios/perfil.html", context)
