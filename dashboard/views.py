from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .models import Product
from .forms import ProductoForm


@login_required
def Dashboard(request):
    productos = Product.objects.filter(created_by=request.user)
    
    total_productos = productos.count()
    stock_bajo = productos.filter(status__in=['low_stock', 'out_of_stock']).count() # Mejor filtro
    
    # Asegúrate de que los tipos de datos sean compatibles para la suma
    # Si 'price' es DecimalField y 'stock' es IntegerField, la multiplicación es segura.
    valor_total_queryset = productos.aggregate(total_value=Sum('price', field='price * stock'))
    valor_total = valor_total_queryset['total_value'] if valor_total_queryset['total_value'] is not None else 0
    
    productos_activos = productos.filter(status='active').count()

    context = {
        'productos': productos,
        'total_productos': total_productos,
        'stock_bajo': stock_bajo,
        'valor_total': round(valor_total, 2),
        'productos_activos': productos_activos
    }
    return render(request, "dashboard/home.html", context)

@login_required
def nuevo_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            nuevo_producto = form.save(commit=False)
            nuevo_producto.created_by = request.user
            nuevo_producto.save() # El método save() del modelo actualizará el estado
            messages.success(request, 'Producto añadido exitosamente.')
            return redirect('dashboard')
    else:
        form = ProductoForm()
        
    return render(request, "dashboard/nuevo.html", {'form': form})

@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Product, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save() # El método save() del modelo actualizará el estado
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('dashboard')
    else:
        form = ProductoForm(instance=producto)
        
    return render(request, "dashboard/editar.html", {'form': form, 'producto': producto})

@login_required
def eliminar_producto(request, pk):
    if request.method == 'POST': # Siempre usa POST para eliminar
        producto = get_object_or_404(Product, pk=pk, created_by=request.user)
        producto.delete()
        messages.success(request, f'Producto "{producto.name}" eliminado exitosamente.')
    return redirect('dashboard')

@login_required
def eliminar_productos_seleccionados(request):
    if request.method == 'POST':
        # Los IDs de los productos vienen como una lista separada por comas en el request
        product_ids = request.POST.getlist('selected_products') 
        
        # Filtramos los productos que pertenecen al usuario y tienen los IDs
        deleted_count, _ = Product.objects.filter(
            pk__in=product_ids, 
            created_by=request.user
        ).delete()
        
        if deleted_count > 0:
            messages.success(request, f'{deleted_count} producto(s) eliminado(s) exitosamente.')
        else:
            messages.warning(request, 'No se seleccionaron productos o no se pudieron eliminar.')
    return redirect('dashboard')


# --- VISTAS DE AUTENTICACIÓN ---
def login_vista(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Bienvenido de nuevo, {username}.")
                return redirect('dashboard')
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    
    form = AuthenticationForm()
    return render(request, "dashboard/login.html", {"form": form})

def registro_vista(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "¡Registro exitoso! Bienvenido.")
            return redirect('dashboard')
        else:
            messages.error(request, "Por favor corrige los errores del formulario.")
    else:
        form = UserCreationForm()
        
    return render(request, "banner/register.html", {"form": form})

def logout_vista(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('login')