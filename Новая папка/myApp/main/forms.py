from typing import Dict, Any

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import News, Registration
from django.forms import *
from django import forms


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'news']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Жаңалық атауы'
            }),
            "news": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Жаңалықты енгізу'
            })
        }


class AddPostForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Registration
        fields = '__all__'

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Пайдаланушы аты', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Электрондық пошта', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Құпия сөз', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Құпия сөзді қайталаңыз', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Есімі', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Тегі', widget=forms.TextInput(attrs={'class': 'form-input'}))
    city = forms.CharField(label='Қала', widget=forms.TextInput(attrs={'class': 'form-input'}))
    address = forms.CharField(label='Мекенжай', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'city', 'address')


class EmailForm(forms.Form):
    email = forms.EmailField(label='Пайдаланушы аты')
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget=forms.Textarea)