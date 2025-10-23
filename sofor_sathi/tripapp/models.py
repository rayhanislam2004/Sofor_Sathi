from django.db import models
from userapp.models import UserProfile
from tourismapp.models import Location


class BucketList(models.Model):

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    spot = models.ForeignKey(Location, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.spot.name} in {self.user.user.username}'s Bucket List"


class Trip(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    spot = models.ForeignKey(Location, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Trip to {self.spot.name} by {self.user.user.username}"


class Budget(models.Model):
    trip = models.OneToOneField(Trip, on_delete=models.CASCADE, related_name='budget')
    transport_cost = models.IntegerField(default=0)
    food_cost = models.IntegerField(default=0)
    hotel_cost = models.IntegerField(default=0)
    other_cost = models.IntegerField(default=0)

    def __str__(self):
        return f"Budget for {self.trip}"
    # it show the trip detail sum of cost
    def total_cost(self):
        return self.transport_cost + self.food_cost + self.hotel_cost + self.other_cost