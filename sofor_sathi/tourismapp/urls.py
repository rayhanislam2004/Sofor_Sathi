from django.urls import path
from . import views

app_name = 'tourismapp'

urlpatterns = [
    # for detail
    path('', views.location_list, name='location_list'),
    path('location/<int:pk>/', views.location_detail, name='location_detail'),
    path('route/<int:route_id>/', views.route_detail, name='route_detail'),

    # for search
    path('search/', views.search_results, name='search_results'),
    path('route-finder/', views.route_finder, name='route_finder'),

    # for review
    path('reviews/', views.review_list_view, name='review_list'),
    path('location/<int:location_id>/add_review/', views.add_location_review, name='add_location_review'),
    path('route/<int:route_id>/add_review/', views.add_route_review, name='add_route_review'),
]
