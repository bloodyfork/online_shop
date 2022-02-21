from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.views import generic


class Register(generic.FormView):
    form_class = UserCreationForm
    template_name = 'Customer/register.html'

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()


class Login:
    pass