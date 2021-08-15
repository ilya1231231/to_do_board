
from .models import Worker, Profile
from django.views.generic import View


class ProfileMixin(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            worker = Worker.objects.filter(user=request.user).first()
            user_profile = Profile.objects.filter(owner=worker).first()


        self.user_profile = user_profile


        return super().dispatch(request, *args, **kwargs)