from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
from django.views import generic


class Register(generic.FormView):
    form_class = UserCreationForm
    template_name = 'Customer/register.html'


class Login:
    pass