from django.urls import path
from customer.API import DeleteAPIAddress, UpdateAPIAddress, CreateAPIAddress, RecentOrdersAPI, UpdateProfileAPI
from customer.views import Login, Register, logout_user, ViewProfile, EditProfile

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('profile/', ViewProfile.as_view(), name='profile'),
    path('EditProfile/', EditProfile.as_view(), name='EditProfile'),
    # API
    # API
    # API
    path('DeleteAddress/<int:pk>', DeleteAPIAddress.as_view(), name='DeleteAddress'),
    path('UpdateAddress/<int:pk>', UpdateAPIAddress.as_view(), name='UpdateAddress'),
    path('CreateAddress/', CreateAPIAddress.as_view(), name='CreateAddress'),
    path('RecentOrders/', RecentOrdersAPI.as_view(), name='RecentOrders'),
    path('UpdateProfile/<int:pk>', UpdateProfileAPI.as_view(), name='UpdateProfile'),

]
