from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.
from .models import Task, Profile, UTask, Worker
from django.views.generic import View
from .mixins import ProfileMixin

from .forms import TaskForm
from .forms import UserRegistrationForm


def index(request):
    tasks = Task.objects.all()  # функция для главной страницы показать сообщение
    return render(request, 'first_app/index.html', {'title': 'Главная страница сайта'})


def about(request):  # Функция для страницы About
    print('yojasjvkbwjkv')
    return render(request, 'first_app/about.html')


def create(request):
    err = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            err = 'Форма была неверной'

    form = TaskForm
    context = {
        'form': form
    }
    return render(request, 'first_app/create.html', context)


class ShowBoardView(ProfileMixin, View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()  # функция для главной страницы показать сообщение
        return render(request, 'first_app/todoboard.html', {'tasks': tasks})


class ProfileView(ProfileMixin, View):

    def get(self, request, *args, **kwargs):
        us_tasks = UTask.objects.filter(profile=self.user_profile)
        context = {
            'user_profile': self.user_profile,
            'us_tasks': us_tasks
        }

        return render(request, 'first_app/user-profile.html', context)


class TakeTodoItemView(ProfileMixin, View):

    def get(self, request, *args, **kwargs):
        i = kwargs.get('i')
        title = Task.objects.get(id=i)
        task = Task.objects.get(id=i).task
        takedtask, created = UTask.objects.get_or_create(
            profile=self.user_profile, u_title=title, u_task=task
        )
        if created:
            self.user_profile.u_individual_task.add(takedtask)
        title.delete()
        self.user_profile.save()
        messages.add_message(request, messages.INFO, 'Вы успешно взяли задание')

        return HttpResponseRedirect('/profile-board/')


class DeleteTaskUserView(ProfileMixin, View):

    def get(self, request, *args, **kwargs):
        i = kwargs.get('i')
        u_task_objects = UTask.objects.get(id=i)
        u_task_objects.delete()
        self.user_profile.save()

        return HttpResponseRedirect('/profile-board/')

