from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField 

class UserProfile(models.Model):
    """
    Model representing a user's profile information.

    Attributes:
        user (User): The user account associated with this profile.
        bio (str): A brief biography of the user, can be blank or null.
        profile_image (CloudinaryField): An optional image representing the user.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.user.username
