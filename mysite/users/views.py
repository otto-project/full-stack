from django.contrib import messages
from django.contrib.auth import authenticate
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


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('main')  # 로그인 후 이동할 페이지
        else:
            messages.error(request, '사용자ID 또는 비밀번호가 잘못되었습니다.')

    return render(request, 'users/login.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form)
            user = form.save()
            # login(request, user)
            return redirect('main')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})
