from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_view
from . import views as users_view

app_name='users'
urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(next_page='/'), name="logout"),
    path('signup/', users_view.signup, name='signup')
]
