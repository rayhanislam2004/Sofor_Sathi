
from django.contrib import admin
from .models import Category, Location, Route, LocationReview, RouteReview

# register models
admin.site.register(Category)
admin.site.register(LocationReview)
admin.site.register(RouteReview)


@admin.action(description='Approve selected items')
def approve_selected(modeladmin, request, queryset):
    queryset.update(is_approved=True)



@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'location',
        'category',
        'submitted_by',
        'is_approved'  
    )

    list_filter = ('is_approved', 'category', 'submitted_by')
    search_fields = ('name', 'location', 'description')

    actions = [approve_selected]


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',  
        'submitted_by',
        'is_approved'
    )
    list_filter = ('is_approved', 'submitted_by', 'location')
    search_fields = ('start_point', 'end_point', 'description')
    actions = [approve_selected]


