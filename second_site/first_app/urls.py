
from django.urls import path, include
from. import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name='home'),
    path('about-me', views.about, name='about'),
    path('create', views.create, name='create'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('todoboard/', views.show_board, name='todoboard'),
    path('take_todo_item/<int:i>/', views.take_todo_item, name='take'),
    path('profile-board/', views.test, name='profiles')


]
