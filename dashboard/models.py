from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    STATUS_CHOICES = [
        ('active', 'Activo'),
        ('low_stock', 'Bajo Stock'),
        ('out_of_stock', 'Agotado'),
    ]
    
    name = models.CharField(max_length=200, verbose_name='Nombre del producto')
    category = models.CharField(max_length=100, verbose_name='Categoría')
    quantity = models.IntegerField(default=0, verbose_name='Cantidad')
    stock = models.IntegerField(default=0, verbose_name='Stock')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active', verbose_name='Estado')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.stock == 0:
            self.status = 'out_of_stock'
        elif self.stock <= 10:
            self.status = 'low_stock'
        else:
            self.status = 'active'
        super().save(*args, **kwargs)

    def get_status_display_custom(self):
        status_map = {
            'active': '● Activo',
            'low_stock': '● Bajo Stock',
            'out_of_stock': '● Agotado',
        }
        return status_map.get(self.status, self.status)
