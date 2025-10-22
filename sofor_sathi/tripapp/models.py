from django.db import models
from userapp.models import UserProfile


class BucketList(models.Model):

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    

class Trip(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

   


class Budget(models.Model):

    trip = models.OneToOneField(Trip, on_delete=models.CASCADE)
    transport_cost = models.IntegerField(default=0)
    food_cost = models.IntegerField(default=0)
    hotel_cost = models.IntegerField(default=0)
    other_cost = models.IntegerField(default=0)

    def __str__(self):
        return f"budget for {self.trip}"
