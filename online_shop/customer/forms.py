from django import forms
from core.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'phone']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'phone', 'password1', 'password2']




#ToDo create login form