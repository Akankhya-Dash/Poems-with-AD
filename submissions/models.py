from django.conf import settings
from django.db import models
from poems.models import MoodTag

User = settings.AUTH_USER_MODEL


class Submission(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    mood = models.ForeignKey(MoodTag, on_delete=models.SET_NULL, null=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.status})"