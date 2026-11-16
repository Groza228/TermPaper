from .models import User
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput


class JoinForm(ModelForm):
    class Meta:
        model = User
        fields = ['login', 'password', 'first_name', 'last_name', 'email']

        widgets = {
            'login': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логін',
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Ім'я"
            }),
            'last_name': TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Прізвище"
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Електронна пошта"
            })
        }


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['login', 'password']
        widgets = {
            'login': TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Логін'
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control', 'placeholder': 'Пароль'
            }),
        }
