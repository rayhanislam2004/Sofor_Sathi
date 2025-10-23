
from django.urls import path
from . import views

app_name = 'contribution'

urlpatterns = [
    path('', views.contribution_hub, name='hub'),
    path('submit/location/', views.submit_location, name='submit_location'),
    path('submit/route/', views.submit_route, name='submit_route'),
]
