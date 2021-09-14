
from django.urls import path, include
from. import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name='home'),
    path('about-me', views.about, name='about'),
    path('create', views.create, name='create'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('todoboard/', views.ShowBoardView.as_view(), name='todoboard'),
    path('take_todo_item/<int:i>/', views.TakeTodoItemView.as_view(), name='take'),
    path('delete_from_profile/<int:i>/', views.DeleteTaskUserView.as_view(), name='delete_from_profile'),
    path('profile-board/', views.ProfileView.as_view(), name='profiles')


]
