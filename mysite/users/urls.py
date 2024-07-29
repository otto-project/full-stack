from django.contrib.auth import views as auth_view
from django.urls import path

from . import views as users_view

app_name = 'users'
urlpatterns = [
    path('login/', users_view.CustomLoginView.as_view(), name="login"),
    path('logout/', auth_view.LogoutView.as_view(next_page='/'), name="logout"),
    path('signup/', users_view.signup, name='signup')
]
