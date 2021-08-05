from django.contrib import admin
from .models import Task
from .models import UTask
from .models import Profile

admin.site.register(Task)
admin.site.register(UTask)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Профиль пользователя'''
    list_display = ('user', 'first_name', 'second_name')



