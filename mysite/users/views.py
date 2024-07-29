from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import SignUpForm


class CustomLoginView(auth_views.LoginView):
    template_name = 'users/login.html'

    def form_invalid(self, form):
        messages.error(self.request, '사용자ID 또는 비밀번호가 잘못되었습니다.')
        return redirect('users:login')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '회원가입 성공!')
            return redirect('main')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})
