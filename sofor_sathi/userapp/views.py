from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('userapp:register')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Account created successfully!")
        return redirect('userapp:login')
    return render(request, 'userapp/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('userapp:profile')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'userapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('userapp:login')

def profile_view(request):
    return render(request, 'userapp/profile.html')
