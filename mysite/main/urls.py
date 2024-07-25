from django.contrib import admin
from django.urls import path
from main import views as main_view

urlpatterns = [
    path('', main_view.index, name="main")
]
