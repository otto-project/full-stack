import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.shortcuts import render
from products.models import ProductTable
from requests.exceptions import Timeout

from .forms import SignUpForm


def request_get(api_url, params):
    try:
        res = requests.get(api_url, params=params, timeout=10)
        return res
    except Timeout as e:
        return None


def load_ml_results(user):
    host = settings.ML_API_HOST
    api_url = f"http://{host}/predict"

    params = {
        "gender": user.gender,
        "weight": user.weight,
        "height": user.height
    }
    products = []
    platforms = ['musinsa', '29cm', 'zigzag']
    categories = ['top', 'bottom']
    for platform in platforms:
        for category in categories:
            temp = ProductTable.get_product_order_by_rank(platform=platform, category=category)
            products.extend(temp)

    for product in products:
        params['product_name'] = product.product_name
        res = request_get(api_url, params)


class CustomLoginView(auth_views.LoginView):
    template_name = "users/login.html"

    def form_valid(self, form):
        user = form.get_user()
        load_ml_results(user)
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
