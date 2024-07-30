from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class SignUpForm(UserCreationForm):
    gender = forms.ChoiceField(choices=CustomUser.GENDER_CHOICES, required=True)
    height = forms.FloatField(required=True)
    weight = forms.FloatField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'gender', 'height', 'weight')
        labels = {
            'username': '아이디'
        }
