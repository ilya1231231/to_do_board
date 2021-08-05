from django.urls import path
#from .views import ProfileCreateView
from .views import test


#app_name = 'profile'

urlpatterns = [
    #path('create/', ProfileCreateView.as_view()),
    #path('userprofile/', profile, name='profile'),
    path('profile-board/', test, name='profiles')

]