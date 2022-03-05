from django import forms

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
        fields = ['first_name', 'phone', 'password1', 'password2']


    def clean_phone(self):

        regex = '(0|\+98)?([ ]|-|[()]){0,2}9[1|2|3|4]([ ]|-|[()]){0,2}(?:[0-9]([ ]|-|[()]){0,2}){8}'

        if re.search(regex, self.cleaned_data.get('phone')) is None:
            raise forms.ValidationError('Please Enter Valid a Phone Number')

        return self.cleaned_data.get('phone')






