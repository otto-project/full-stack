import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.shortcuts import render
from requests.exceptions import Timeout

from .forms import SignUpForm


def request_get(api_url, params):
    try:
        res = requests.get(api_url, params=params, timeout=10)
        return res
    except Timeout as e:
        return None


class CustomLoginView(auth_views.LoginView):
    template_name = "users/login.html"

    def form_valid(self, form):
        host = settings.ML_API_HOST
        user = form.get_user()
        height = user.height
        weight = user.weight
        api_url = f"http://{host}/predict"
        params = {
            'height': height,
            'weight': weight
        }
        res = request_get(api_url, params)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "사용자ID 또는 비밀번호가 잘못되었습니다.")
        return self.get(self.request)


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "회원가입 성공!")
            return redirect('main_platform', platform='musinsa')
    else:
        form = SignUpForm()
    return render(request, "users/signup.html", {"form": form})
