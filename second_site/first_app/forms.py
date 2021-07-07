

from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User
from django import forms

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






class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']





