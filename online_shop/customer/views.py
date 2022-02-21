# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

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
            return redirect(to='register')


class Login:
    pass
