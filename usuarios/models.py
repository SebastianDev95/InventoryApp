from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def avatar_upload_path(instance, filename):
    return f"avatars/user_{instance.user.id}/{filename}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=avatar_upload_path, blank=True, null=True)
    mensaje = models.TextField(blank=True, verbose_name="Mensaje de bienvenida")
    idioma = models.CharField(max_length=20, default='Español')
    hora = models.CharField(max_length=20, default='24h')
    pais = models.CharField(max_length=50, default='Colombia')
    zona = models.CharField(max_length=50, default='UTC -5 Bogotá')
    
    # 👇 Aquí agregas el campo nuevo (Opción 1)
    genero = models.CharField(max_length=20, default='Otro', blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

    @property
    def avatar_url(self):
        """Devuelve la URL del avatar o una imagen predeterminada."""
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        return '/static/img/default_male.png'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
