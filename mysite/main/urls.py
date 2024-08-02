from django.urls import path

from . import views as main_view

urlpatterns = [
    path('', main_view.main_musinsa, name="main"),
    path('musinsa/', main_view.main_musinsa, name="main_musinsa"),
    path('29cm/', main_view.main_29cm, name="main_29cm"),
    path('zigzag/', main_view.main_zigzag, name="main_zigzag"),
]
