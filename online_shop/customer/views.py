# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import CreateUserForm
# Create your views here.
from django.views import generic


class Register(generic.FormView):
    form_class = CreateUserForm
    template_name = 'Customer/register.html'

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account has been created with username " + username)
            return redirect(to='login')

        else:
            messages.warning(request, 'wrong input!')
            return redirect(to='register')


class Login(generic.FormView):
    form_class = CreateUserForm
    template_name = "Customer/login.html"


