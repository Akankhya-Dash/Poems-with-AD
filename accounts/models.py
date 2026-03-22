from django.db import models

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
