from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.timezone import now
from .models import Poem


@receiver(pre_save, sender=Poem)
def set_published_at(sender, instance, **kwargs):
    if instance.is_published and not instance.published_at:
        instance.published_at = now()