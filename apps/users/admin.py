from django.contrib import admin
from .models import User, Todo

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'age']

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'is_completed', 'created_at', 'image']
