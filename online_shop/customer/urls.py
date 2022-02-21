from django.urls import path, include

from customer.views import Login, Register

urlpatterns = [
    path('login/', Login, name='login'),
    path('register/', Register.as_view(), name='register'),

]