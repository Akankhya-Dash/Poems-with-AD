from django.conf import settings
from django.db import models
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL


class MoodTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    color_code = models.CharField(max_length=7, blank=True)
    intensity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Poem(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='poems')
    mood = models.ForeignKey(MoodTag, on_delete=models.SET_NULL, null=True, related_name='poems')

    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    ambient_audio_url = models.URLField(blank=True)
    reading_time = models.PositiveIntegerField(default=30)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True) 
    is_approved = models.BooleanField(default=False) 

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['is_published', 'created_at']),
            models.Index(fields=['mood']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            # NOTE: In production, handle duplicate slugs with suffix logic
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
