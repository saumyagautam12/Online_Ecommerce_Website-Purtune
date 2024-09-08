from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm

from .models import *
from django import forms
from django.forms.widgets import PasswordInput
# from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email","Name","password1","password2")



# class LoginForm(AuthenticationForm):
#     username=forms.CharField()
#     password=forms.CharField(widget=PasswordInput())

#     class Meta:
#         model = User
#         # fields = ("email","first_name","last_name","phone",)
#         fields = ('username','password')
