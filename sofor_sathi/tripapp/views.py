from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from tourismapp.models import Location
from .models import BucketList, Trip, Budget
from .forms import TripForm, BudgetForm


@login_required
def add_to_bucket_list(request, location_id):
    location = get_object_or_404(Location, id=location_id)

    if not BucketList.objects.filter(user=request.user.userprofile, spot=location).exists():
        BucketList.objects.create(user=request.user.userprofile, spot=location)
        messages.success(request, f'"{location.name}" added to your bucket list!')
    else:
        messages.warning(request, f'"{location.name}"  already in your bucket list.')

    return redirect('tourismapp:location_detail', pk=location_id)


@login_required
def plan_trip(request, location_id):
    location = get_object_or_404(Location, id=location_id)


    if request.method == 'POST':
        trip_form = TripForm(request.POST)
        budget_form = BudgetForm(request.POST)

        if trip_form.is_valid() and budget_form.is_valid():

            trip = trip_form.save(commit=False)

            trip.user = request.user.userprofile
            trip.spot = location
            trip.save()
            budget = budget_form.save(commit=False)
            budget.trip = trip
            budget.save()

            messages.success(request, f"Your trip to {location.name} has been planned")

            return redirect('userapp:profile')

    else:
        trip_form = TripForm()
        budget_form = BudgetForm()

    context = {
        'location': location,
        'trip_form': trip_form,
        'budget_form': budget_form
    }
    return render(request, 'tripapp/plan_trip.html', context)


@login_required
def bucket_list_view(request):
    bucket_list_items = BucketList.objects.filter(user=request.user.userprofile)
    context = {'bucket_list_items': bucket_list_items}
    return render(request, 'tripapp/bucket_list.html', context)


@login_required
def trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)

    if trip.user != request.user.userprofile:
        messages.error(request, "You are not authorized to view this trip.")
        return redirect('userapp:profile')


    context = {
        'trip': trip
    }
    return render(request, 'tripapp/trip_detail.html', context)