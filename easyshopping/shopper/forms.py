from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Shop


class SearchForm(forms.ModelForm):
    class Meta:
        model = Shop
        exclude = ()
        fields = ['title',]
        widgets = {
            'title': forms.TextInput()
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())