
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LocationSubmissionForm, RouteSubmissionForm
from tourismapp.models import Location


@login_required
def contribution_hub(request):
    return render(request, 'contribution/hub.html')


@login_required
def submit_location(request):
    if request.method == 'POST':
        form = LocationSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            location = form.save(commit=False)
            location.submitted_by = request.user.userprofile
            location.is_approved = False
            location.save()
            messages.success(request, 'your location has been submitted for review.')
            return redirect('contribution:hub')
    else:
        form = LocationSubmissionForm()
    return render(request, 'contribution/submission_form.html', {'form': form, 'title': 'suggest a new location'})



@login_required
def submit_route(request):
    if request.method == 'POST':
        form = RouteSubmissionForm(request.POST)
        form.fields['location'].queryset = Location.objects.filter(is_approved=True)

        if form.is_valid():
            route = form.save(commit=False)
            route.submitted_by = request.user.userprofile
            route.is_approved = False
            route.save()
            messages.success(request, 'your route has been submitted for review.')
            return redirect('contribution:hub')


    else:
        form = RouteSubmissionForm()

        form.fields['location'].queryset = Location.objects.filter(is_approved=True)

    return render(request, 'contribution/submission_form.html', {'form': form, 'title': 'suggest a new route'})
