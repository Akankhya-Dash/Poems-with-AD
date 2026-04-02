from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('writer', 'Writer'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='writer')
    bio = models.TextField(blank=True)
    is_verified_writer = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='profile')
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    @property
    def display_pic(self):
        """
        Returns the profile picture if exists,
        else returns the poet's image if available,
        else returns None.
        """
        if self.profile_pic:
            return self.profile_pic.url
        # Fallback to poet image
        try:
            return self.user.poet.image.url
        except (AttributeError, ValueError):
            return None
