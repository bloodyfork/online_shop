from django.urls import path, include

from customer.views import Login, Register, logout_user

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', Register.as_view(), name='register'),

]