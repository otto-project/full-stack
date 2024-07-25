from django.shortcuts import render
from django.shortcuts import redirect
from .forms import SignUpForm

# Create your views here.
def login(request):
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
