from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import SignUpForm


class CustomLoginView(auth_views.LoginView):
    template_name = "users/login.html"

    # def form_valid(self, form):
    #     host = settings.ML_API_HOST
    #     api_url = f"http://{host}/predict?height=150&weight=10"
    #     res = requests.get(api_url)
    #     print(res)

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
