from django import forms
from .models import Shop


class SearchForm(forms.ModelForm):
    class Meta:
        model = Shop
        exclude = ()
        fields = ['title',]
        widgets = {
            'title': forms.TextInput()
        }
