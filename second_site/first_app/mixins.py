from .models import Worker, Profile
from django.views.generic import View


class ProfileMixin(View):
    ''' Миксин для для аутентификации пользователя '''
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            worker = Worker.objects.filter(user=request.user).first()
            user_profile = Profile.objects.filter(owner=worker).first()
        self.user_profile = user_profile


        return super().dispatch(request, *args, **kwargs)

class WorkerMixin(View):
    ''' Миксин для для аутентификации пользователя '''
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            worker_card = Worker.objects.filter(user=request.user)
        self.worker_card = worker_card


        return super().dispatch(request, *args, **kwargs)
