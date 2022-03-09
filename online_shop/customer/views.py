from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Customer
from .forms import CreateUserForm
# Create your views here.


class Register(generic.FormView):
    form_class = CreateUserForm
    template_name = 'Customer/register.html'

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            phone = form.cleaned_data.get('phone')
            messages.success(request, "Account has been created with phone number " + phone)
            return redirect(to='login')

        else:
            e = form.errors
            print(form.cleaned_data)

            messages.warning(request, e)
            return redirect(to='register')


class Login(LoginView):
    template_name = "Customer/login.html"

    def post(self, request, *args, **kwargs):

        username = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            Customer.objects.get_or_create(user=user)
            login(request, user)
            return redirect(to='home')

        else:
            messages.info(request, "incorrect Password or Username")
            return render(request, 'Customer/login.html')


def logout_user(request):
    logout(request)
    return redirect(to='login')


@login_required(login_url='login')
def view_profile(request):
    return render(request, 'Customer/View_profile.html')
