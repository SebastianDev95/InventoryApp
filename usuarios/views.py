from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
import os

@login_required
def perfil(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        mensaje = request.POST.get("mensaje")
        idioma = request.POST.get("idioma")
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

        # --- Guardar datos del usuario ---
        user.first_name = nombre
        user.save()

        profile.mensaje = mensaje
        profile.idioma = idioma
        profile.hora = hora
        profile.pais = pais
        profile.zona = zona
        profile.save()

        messages.success(request, "✅ Cambios guardados correctamente.")
        return redirect("perfil")

    # --- Textos dinámicos según idioma ---
    texts = {
        "Español": {"title": "Configuración de la Cuenta", "welcome": "¡Bienvenido a tu perfil!", "save": "Guardar", "cancel": "Cancelar"},
        "Inglés": {"title": "Account Settings", "welcome": "Welcome to your profile!", "save": "Save", "cancel": "Cancel"},
        "Francés": {"title": "Paramètres du Compte", "welcome": "Bienvenue sur votre profil!", "save": "Enregistrer", "cancel": "Annuler"},
    }

    lang = profile.idioma or "Español"
    text = texts.get(lang, texts["Español"])

    context = {
        "nombre": user.first_name or user.username,
        "mensaje": profile.mensaje or text["welcome"],
        "idioma": profile.idioma,
        "hora": profile.hora,
        "pais": profile.pais,
        "zona": profile.zona,
        "text": text,
        "avatar_url": profile.avatar_url,
    }

    return render(request, "usuarios/perfil.html", context)
