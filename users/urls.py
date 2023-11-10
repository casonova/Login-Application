from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import *

urlpatterns = [
    path('',SignupView.as_view(),name=""),
    path('signup/', SignupView.as_view(),name='signup'),
    path('login/',LoginView.as_view(),name="login"),
    path('index/', HomeView.as_view(), name='index'),
    path('update/', UpdateView.as_view(), name='update'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    
]