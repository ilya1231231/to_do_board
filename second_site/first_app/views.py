from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.
from .models import Task, Profile, UTask


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


def take_todo_item(request, i):

    title = Task.objects.get(id=i)
    task = Task.objects.get(id=i).task
    user_profile = Profile.objects.get(
        user=request.user
    )
    takedtask, created = UTask.objects.get_or_create(
        u_title=title, u_task=task, object_id=i
    )
    if created:
        user_profile.u_individual_task.add(takedtask)

    user_profile.save()

    return HttpResponseRedirect('/profile-board/')




def test(request):     # username):
    #users = User.objects.filter(username=pk)
    #u = User.objects.get(username=username)
    #show = Profile.objects.all()
    #url = reverse('profile/user-profile.html', kwargs={'username': u})

    #print(Profile.objects.filter(user=users[0].id)[0])

    return render(request, 'first_app/user-profile.html')










