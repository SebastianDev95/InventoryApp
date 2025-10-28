from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'username', 'is_staff', 'date_joined']
    search_fields = ['email', 'first_name', 'username']
    ordering = ['-date_joined']
