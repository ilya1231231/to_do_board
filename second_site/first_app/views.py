from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Task, Profile, UTask, Worker
from django.views.generic import View
from .mixins import ProfileMixin, WorkerMixin
from .forms import TaskForm, WorkerCardForm


# from .forms import UserRegistrationForm


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


class ShowBoardView(WorkerMixin, ProfileMixin, View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()  # функция для главной страницы показать сообщение
        user_name = Worker.objects.get(user=request.user)
        return render(request, 'first_app/todoboard.html', {'tasks': tasks, 'user_name': user_name})


class ProfileView(WorkerMixin, ProfileMixin, View):

    def get(self, request, *args, **kwargs):
        us_tasks = UTask.objects.filter(profile=self.user_profile)
        context = {
            'worker_card': self.worker_card,
            'user_profile': self.user_profile,
            'us_tasks': us_tasks
        }

        return render(request, 'first_app/user-profile.html', context)


class TakeTodoItemView(WorkerMixin, ProfileMixin, View):

    def get(self, request, *args, **kwargs):
        i = kwargs.get('i')
        title = Task.objects.get(id=i)
        task = Task.objects.get(id=i).task
        UTask.objects.create(
            profile=self.user_profile, u_title=title, u_task=task
        )
        title.delete()
        self.user_profile.save()
        messages.add_message(request, messages.INFO, 'Вы успешно взяли задание')

        return HttpResponseRedirect('/profile-board/')


class DeleteTaskUserView(WorkerMixin, ProfileMixin, View):

    def get(self, request, *args, **kwargs):
        i = kwargs.get('i')
        u_task_objects = UTask.objects.get(id=i)
        u_task_objects.delete()
        self.user_profile.save()

        return HttpResponseRedirect('/profile-board/')


class WorkerCardView(WorkerMixin, ProfileMixin, View):
    def get(self, request, *args, **kwargs):
        form = WorkerCardForm
        context = {
            'worker_card': self.worker_card,
            'form': form
        }
        current_user = request.user
        print(current_user.id)
        return render(request, 'first_app/worker_card.html', context)

    def sample_view(self, request):
        current_user = request.user
        print(current_user.id)


class WorkerCardAdd(WorkerMixin, ProfileMixin, View):
    def post(self, request, *args, **kwargs):
        form = WorkerCardForm(request.POST, request.FILES)
        current_user = request.user
        if form.is_valid():
            work_card = form.save(commit=False)
            work_card.user = request.user
            work_card.save()

            return HttpResponseRedirect('/')

        return HttpResponseRedirect('/')
