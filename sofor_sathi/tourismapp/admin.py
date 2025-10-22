
from django.contrib import admin
from .models import Category, Location, Route, LocationReview, RouteReview

# register models
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Route)
admin.site.register(LocationReview)
admin.site.register(RouteReview)
