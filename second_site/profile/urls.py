from django.urls import path
#from .views import ProfileCreateView
from .views import Test


#app_name = 'profile'

urlpatterns = [
    #path('create/', ProfileCreateView.as_view()),
    #path('userprofile/', profile, name='profile'),
    path('test/<str:pk>/', Test)

]