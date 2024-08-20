from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm

from .models import *
from django import forms
from django.forms.widgets import PasswordInput
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username","email","password1","password2")


class LoginForm(AuthenticationForm):
    username=forms.CharField()
    password=forms.CharField(widget=PasswordInput())

    class Meta:
        model = User
        # fields = ("email","first_name","last_name","phone",)
        fields = ('username','password')
