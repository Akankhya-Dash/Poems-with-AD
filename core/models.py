from django.db import models
from django.conf import settings
#from poems.models import User

# Create your models here.
class Poet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='poets/')
    
    
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import Poet

# @receiver(post_save, sender=User)
# def create_poet(sender, instance, created, **kwargs):
#     if created:
#         Poet.objects.create(
#             user=instance,
#             name=instance.username,
#             slug=instance.username
#         )