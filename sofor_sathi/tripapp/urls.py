from django.urls import path
from . import views


app_name = 'tripapp'

urlpatterns = [

    path('bucket/add/<int:location_id>/', views.add_to_bucket_list, name='add_to_bucket_list'),

    path('bucket/', views.bucket_list_view, name='bucket_list'),

    path('plan/<int:location_id>/', views.plan_trip, name='plan_trip'),
]
