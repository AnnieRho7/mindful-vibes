from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField 

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.user.username
