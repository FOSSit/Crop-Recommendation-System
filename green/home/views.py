from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            messages.success(request, 'Your account has been created successfully.')
            return redirect('login')

    return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome back!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('index')

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('login')

def afilter(request):
    return render(request, 'afilter.html')

def result(request):
    return render(request, 'result.html')
