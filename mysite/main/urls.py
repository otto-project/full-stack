from django.urls import path

from . import views as main_view

urlpatterns = [
    path('', main_view.index, name="main")
]
