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
    tasks = Task.objects.all()     # функция для главной страницы показать сообщение
    return render(request, 'first_app/index.html', {'title': 'Главная страница сайта' })



def about(request):    #Функция для страницы About
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
        return render(request, 'first_app/todoboard.html',{'tasks': tasks})


class ProfileView(ProfileMixin, View):

    def get(self, request, *args, **kwargs):
        context = {
            'user_profile': self.user_profile
        }

        return render(request, 'first_app/user-profile.html', context)


class TakeTodoItemView(ProfileMixin, View):

    def get(self, request, *args, **kwargs):
        i = kwargs.get('i')
        title = Task.objects.get(id=i)
        task = Task.objects.get(id=i).task
        print(i)
        # worker = Worker.objects.get(user=request.user)
        # user_profile = Profile.objects.get(owner=worker)
        takedtask, created = UTask.objects.get_or_create(
            user=self.user_profile.owner, u_title=title, u_task=task
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
        u_title = UTask.objects.get(id=i)
        print(i)
        worker = Worker.objects.get(user=request.user)
        user_profile = Profile.objects.get(owner=worker)
        takedtask, created = UTask.objects.get_(
            u_title=title, u_task=task
        )
        # if created:
        #     self.user_profile.u_individual_task.add(takedtask)
        u_title.delete()
        self.user_profile.save()
        messages.add_message(request, messages.INFO, 'Вы успешно удалили задание')

        return HttpResponseRedirect('/profile-board/')














