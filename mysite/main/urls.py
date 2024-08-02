from django.urls import path

from . import views as main_view

urlpatterns = [
    path('', main_view.index, name='index'),
    path('<str:platform>/', main_view.main_platform, name='main_platform'),
]
