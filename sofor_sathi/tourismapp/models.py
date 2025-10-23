from django.db import models
from userapp.models import UserProfile


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='locations/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='locations')
     # for user contribution
    is_approved = models.BooleanField(default=False)
    submitted_by = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='submitted_locations'
    )

    def __str__(self):
        return f"{self.name} ({self.location})"


class Route(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='routes')
    start_point = models.CharField(max_length=255)
    end_point = models.CharField(max_length=255)
    description = models.TextField(help_text="Provide details about the transport type, fare, and time.")
     # for user contribution
    is_approved = models.BooleanField(default=False)
    submitted_by = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,null=True,
        blank=True,
        related_name='submitted_routes'
    )

    def __str__(self):
        return f"Route from {self.start_point} to {self.location.name}"


class LocationReview(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.user.username} for {self.location.name}"


class RouteReview(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.user.username} for route to {self.route.location.name}"
