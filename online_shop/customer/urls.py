from django.urls import path, include

from customer.views import login_page, Register

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', Register.as_view(), name='register'),

]