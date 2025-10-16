from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)
    language_preference = models.CharField(max_length=50, default='English')
    total_visited = models.IntegerField(default=0)
    wishlist_count = models.IntegerField(default=0)

    TRAVEL_CHOICES = [
        ('Adventure', 'Adventure'),
        ('Cultural', 'Cultural'),
        ('Relaxation', 'Relaxation'),
        ('Nature', 'Nature'),
        ('Historical', 'Historical'),
    ]
    travel_preference = models.CharField(
        max_length=50,
        choices=TRAVEL_CHOICES,
        default='Nature',
        help_text="Select your preferred type of travel"
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # create profile on user creation, ensure profile exists on save
    if created:
        UserProfile.objects.create(user=instance)
    else:

        try:
            instance.userprofile.save()
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=instance)
