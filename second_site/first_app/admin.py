from django.contrib import admin

from .models import Task
from .models import UTask
from .models import Profile, Worker


admin.site.register(Task)
admin.site.register(UTask)
admin.site.register(Worker)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Профиль пользователя'''
    list_display = ('owner', 'first_name', 'second_name')

