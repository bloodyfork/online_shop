from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from core.models import User
from django.contrib.auth.forms import UserCreationForm
import re


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'phone']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'phone', 'password1', 'password2']
        widgets = {"phone": forms.TextInput()}

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if re.search('(0|\+98)?([ ]|-|[()]){0,2}9[1|2|3|4]([ ]|-|[()]){0,2}(?:[0-9]([ ]|-|[()]){0,2}){8}',
                     phone) is not None:
            pass

        else:
            raise ValidationError('Please Enter a valid phone')
