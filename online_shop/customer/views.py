from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import generic
from .models import Customer, Address
from .forms import CreateUserForm
from django.views.generic.list import ListView
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


class ViewProfile(ListView, LoginRequiredMixin):
    model = Address
    template_name = 'Customer/view_profile.html'
    context_object_name = 'addresses'

    def get_queryset(self):
        query = Address.objects.filter(customer__user=self.request.user)
        return query



# @login_required(login_url='login')
# def view_profile(request):
#     data = Address.objects.filter(customer__user=request.user)
#     context = {'data': data}
#     return render(request, 'Customer/View_profile.html', context)
