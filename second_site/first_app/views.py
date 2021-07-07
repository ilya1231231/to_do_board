from django.shortcuts import render, redirect
# Create your views here.
from .models import Task

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


def show_board(request):
    tasks = Task.objects.all()  # функция для главной страницы показать сообщение
    return render(request, 'first_app/todoboard.html',{'tasks': tasks})











