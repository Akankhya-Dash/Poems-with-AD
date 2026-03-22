from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Submission
from poems.models import Poem


@receiver(post_save, sender=Submission)
def create_poem_on_approval(sender, instance, created, **kwargs):
    if instance.status == 'approved':
        if not Poem.objects.filter(title=instance.title, author=instance.submitted_by).exists():
            Poem.objects.create(
                title=instance.title,
                content=instance.content,
                author=instance.submitted_by,
                mood=instance.mood,
                is_published=True
            )