from .models import Task, Worker
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User
from django import forms


# from django import forms

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {"title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название'
        }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }


class WorkerCardForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = (
            'first_name',
            'second_name',
            'last_name',
            'birthday',
            'birthday_place',
            'foreign_languages',
            'education',
            'avatar'
        )
