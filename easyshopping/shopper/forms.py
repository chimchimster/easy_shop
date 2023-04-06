from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Shop


class SearchForm(forms.ModelForm):
    class Meta:
        model = Shop
        exclude = ()
        fields = ['title',]
        widgets = {
            'title': forms.TextInput()
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput())
    email = forms.CharField(label='Электронная почта', widget=forms.EmailInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    repeat_password = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput())