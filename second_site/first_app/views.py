from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.
from .models import Task
from django.views.generic import View
from .forms import TaskForm
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from .models import Profile, UTask



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


def show_board(request):
    tasks = Task.objects.all()  # функция для главной страницы показать сообщение
    return render(request, 'first_app/todoboard.html', {'tasks': tasks})


def TakeTaskView(request, i):
    pkr = Task.objects.get(id=i)
    person = Task.objects.all()
    user_profile = Profile.objects.get(
        user=request.user
    )
    takedtask, created = UTask.objects.get_or_create(
        usr_title=pkr
    )
    if created:
        user_profile.user_task_title.add(takedtask)

    print(str(person))

    return HttpResponseRedirect('/todoboard/')



def test(request):     # username):
    #users = User.objects.filter(username=pk)
    #u = User.objects.get(username=username)
    #show = Profile.objects.all()
    #url = reverse('profile/user-profile.html', kwargs={'username': u})

    #print(Profile.objects.filter(user=users[0].id)[0])

    return render(request, 'first_app/user-profile.html') #username)













