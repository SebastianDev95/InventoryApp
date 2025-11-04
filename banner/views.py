from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import RegisterForm, EmailLoginForm

User = get_user_model()

def register_view(request):
    """
    Maneja el registro de usuarios
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'¡Bienvenido, {user.first_name}! Tu cuenta ha sido creada.')
            return redirect('dashboard')
        else:
            # Muestra los errores específicos del formulario
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = RegisterForm()
    
    return render(request, 'banner/register.html', {'form': form})


def login_view(request):
    """
    Maneja el inicio de sesión de usuarios
    """
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            messages.success(request, f'¡Bienvenido de nuevo, {user.first_name}!')
            return redirect('dashboard')
        else:
            for error in form.non_field_errors():
                messages.error(request, error)
            for field, errors in form.errors.items():
                 if field != '__all__':
                    for error in errors:
                        messages.error(request, f'{field.capitalize()}: {error}')
    else:
        form = EmailLoginForm()

    return render(request, 'banner/login.html', {'form': form})


@login_required
def logout_view(request):
    """
    Maneja el cierre de sesión
    """
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('login') 


def index(request):
    """
    Vista de la página principal
    """
    return render(request, "banner/index.html")