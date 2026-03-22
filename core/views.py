from django.shortcuts import render, get_object_or_404
from poems.models import Poem, MoodTag


def base_queryset():
    return (
        Poem.objects.filter(is_published=True)
        .select_related('author', 'mood')
        .order_by('-is_featured', '-created_at')
    )


def home_view(request):
    poems = base_queryset()
    moods = MoodTag.objects.all()

    return render(request, 'home.html', {
        'poems': poems,
        'moods': moods
    })


def mood_view(request, mood_name):
    mood = get_object_or_404(MoodTag, name=mood_name)

    poems = base_queryset().filter(mood=mood)

    return render(request, 'home.html', {
        'poems': poems,
        'moods': MoodTag.objects.all(),
        'active_mood': mood_name
    })