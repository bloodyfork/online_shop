from django.urls import path

from customer.views import Login, Register, logout_user, view_profile

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('profile/', view_profile, name='profile'),


]