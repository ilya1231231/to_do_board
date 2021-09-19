from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    Логин = forms.CharField()
    Пароль = forms.CharField(widget=forms.PasswordInput)






class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароль не подходит')
        return cd['password2']