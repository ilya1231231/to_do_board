from .models import Profile

from django.contrib import admin

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Профиль пользователя'''
    list_display = ('user', 'first_name', 'second_name')
