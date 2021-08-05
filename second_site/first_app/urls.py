
from django.urls import path, include
from .views import show_board, create, about, index, TakeTaskView, test
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', index, name='home'),
    path('about-me', about, name='about'),
    path('create', create, name='create'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('todoboard/', show_board, name='todoboard'),
    path('profile-board/', test, name='profiles'),
    path('take/<int:i>/', TakeTaskView, name='take')
]
