from django.shortcuts import render, redirect, get_object_or_404
from .models import Location, Route, LocationReview, RouteReview
from .forms import LocationReviewForm, RouteReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def location_list(request):
    locations = Location.objects.filter(is_approved=True)
    context = {'locations': locations}
    return render(request, 'tourismapp/location_list.html', context)


def location_detail(request, pk):
    location = get_object_or_404(Location, pk=pk, is_approved=True)
    location_review_form = LocationReviewForm()
    route_review_form = RouteReviewForm()
    approved_routes = location.routes.filter(is_approved=True)

    context = {
        'location': location,
        'location_review_form': location_review_form,
        'route_review_form': route_review_form,
        'approved_routes': approved_routes,
    }
    return render(request, 'tourismapp/location_detail.html', context)


@login_required
def add_location_review(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    if request.method == 'POST':
        form = LocationReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.location = location
            review.user = request.user.userprofile
            review.save()
            messages.success(request, 'Your review has been added!')
            return redirect('tourismapp:location_detail', pk=location.id)
    return redirect('tourismapp:location_detail', pk=location.id)


@login_required
def add_route_review(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    location = route.location
    if request.method == 'POST':
        form = RouteReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.route = route
            review.user = request.user.userprofile
            review.save()
            messages.success(request, 'Your route review has been added!')
            return redirect('tourismapp:location_detail', pk=location.id)
    return redirect('tourismapp:location_detail', pk=location.id)


def search_results(request):
    query = request.GET.get('q')
    results = Location.objects.none()

    if query:

        name_results = Location.objects.filter(name__icontains=query)
        location_results = Location.objects.filter(location__icontains=query)
        results = name_results | location_results
        results = results.filter(is_approved=True).distinct()

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'tourismapp/search_results.html', context)



@login_required
def route_detail(request, route_id):
    route = get_object_or_404(Route, id=route_id, is_approved=True)
    if request.method == 'POST':
        form = RouteReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.route = route
            review.user = request.user.userprofile
            review.save()
            messages.success(request, 'Your review for this route has been added!')
            return redirect('tourismapp:route_detail', route_id=route.id)
    else:
        form = RouteReviewForm()
    context = {
        'route': route,
        'form': form,
    }
    return render(request, 'tourismapp/route_detail.html', context)


def route_finder(request):
    start_point_filter = request.GET.get('start_point')
    end_point_filter = request.GET.get('end_point')

    routes = Route.objects.filter(is_approved=True)
    start_points = routes.values_list('start_point', flat=True).distinct()
    end_points = routes.values_list('end_point', flat=True).distinct()

    if start_point_filter and start_point_filter != '':
        routes = routes.filter(start_point=start_point_filter)

    if end_point_filter and end_point_filter != '':
        routes = routes.filter(end_point=end_point_filter)

    context = {
        'start_points': start_points,
        'end_points': end_points,
        'routes': routes,
        'selected_start': start_point_filter,
        'selected_end': end_point_filter,
    }
    return render(request, 'tourismapp/route_finder.html', context)


def review_list_view(request):
    location_reviews = LocationReview.objects.filter(location__is_approved=True).order_by('-id')
    route_reviews = RouteReview.objects.filter(route__is_approved=True).order_by('-id')

    context = {
        'location_reviews': location_reviews,
        'route_reviews': route_reviews,
    }
    return render(request, 'tourismapp/review_list.html', context)
