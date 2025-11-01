from django import forms
from .models import Product

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Product
        # Aseguramos que los campos coincidan con tu modelo
        fields = ['name', 'category', 'quantity', 'stock', 'price']
        
        # Opcional: Esto ayuda a que las etiquetas coincidan si son diferentes
        labels = {
            'name': 'Nombre del producto',
            'category': 'Categoría',
            'quantity': 'Cantidad',
            'stock': 'Stock',
            'price': 'Precio',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Asignamos los IDs y atributos de tu HTML a los campos del formulario
        self.fields['name'].widget.attrs.update({'id': 'productName', 'required': True})
        self.fields['category'].widget.attrs.update({'id': 'category', 'required': True})
        self.fields['quantity'].widget.attrs.update({'id': 'quantity', 'required': True})
        self.fields['stock'].widget.attrs.update({'id': 'stock', 'required': True})
        self.fields['price'].widget.attrs.update({'id': 'price', 'step': '0.01', 'required': True})