from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserProfileForm
from tourismapp.models import LocationReview, RouteReview
from tripapp.models import BucketList, Trip


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'account created successfully. Please login.')
            return redirect('userapp:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'userapp/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=uname, password=pwd)
        if user:
            login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('userapp:profile')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'userapp/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('userapp:login')


@login_required
def profile_view(request):
    profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('userapp:profile')
    else:
        form = UserProfileForm(instance=profile)


    location_reviews = LocationReview.objects.filter(user=profile)
    route_reviews = RouteReview.objects.filter(user=profile)
    bucket_list_items = BucketList.objects.filter(user=profile)
    planned_trips = Trip.objects.filter(user=profile).order_by('-start_date')

    context = {
        'profile': profile,
        'form': form,
        'location_reviews': location_reviews,
        'route_reviews': route_reviews,
        'bucket_list_items': bucket_list_items,
        'planned_trips': planned_trips,
    }

    return render(request, 'userapp/profile.html', context)
