from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_view
from . import views as users_view

app_name='users'
urlpatterns = [
    path('', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('signup/', users_view.signup, name='signup')
]
