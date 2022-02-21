from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.models import User
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


class Login(LoginView):
    template_name = "Customer/login.html"

    def post(self, request, *args, **kwargs):

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(to='home')

        else:
            messages.info(request, "incorrect Password or Username")
            return render(request, 'Customer/login.html')


def logout_user(request):
    logout(request)
    return redirect(to='login')


# def login_page(request):
#
#     if request.method == "POST":
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect(to='home')
#
#             else:
#                 messages.info(request, "incorrect Password or Username")
#
#     return render(request, 'Customer/login.html')

@login_required(login_url='login')
class ViewProfile(generic.DetailView):
    model = User
    template_name = 'Customer/View_profile.html'
