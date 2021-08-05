from .models import Profile
from django.forms import ModelForm, TextInput


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'second_name']
        widgets = {"first_name": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ваше имя'
        }),
            "second_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ваша фамилия'
            }),
        }