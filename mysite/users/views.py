import requests
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.shortcuts import render
from products.models import ProductTable
from requests.exceptions import Timeout

from .forms import SignUpForm
from .models import UserMLResult


def request_get(api_url, params):
    try:
        res = requests.get(api_url, params=params, timeout=3)
        return res
    except Timeout as e:
        return None


def connection_test(api_url):
    try:
        requests.get(api_url, timeout=10)
        return True
    except Timeout as e:
        return False
    except ConnectionError as e:
        return False


def load_ml_results(user):
    host = settings.ML_API_HOST
    api_url = f"http://{host}/predict"
    connection_url = f"http://{host}/connection"

    if not UserMLResult.needs_api_call(user):
        return

    if not connection_test(connection_url):
        return

    gender = '남성' if user.gender == 'male' else '여성'
    params = {
        "gender": gender,
        "weight": user.weight,
        "height": user.height
    }
    products = []
    platforms = ['musinsa', '29cm', 'zigzag']
    categories = ['top', 'bottom']
    for platform in platforms:
        for category in categories:
            temp = ProductTable.get_product_filter_by_gender(platform=platform, category=category, gender=user.gender)
            products.extend(temp)

    for product in products:
        params['product_name'] = product.product_name
        res = request_get(api_url, params)
        size, score = process_prediction_result(res)
        UserMLResult.create(user=user, product=product, size=size, score=score)


def process_prediction_result(res):
    if res is None:
        return '-', 0
    res = res.json()
    if not res or not res['success']:
        return '-', 0
    return res['prediction'], res['prob']


class CustomLoginView(auth_views.LoginView):
    template_name = "users/login.html"

    def form_valid(self, form):
        user = form.get_user()
        load_ml_results(user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.get(self.request)


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_platform', platform='musinsa')
    else:
        form = SignUpForm()
    return render(request, "users/signup.html", {"form": form})
