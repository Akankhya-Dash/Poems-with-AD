from django.shortcuts import render, get_object_or_404,redirect
from poems.models import Poem, MoodTag
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from poems.forms import PoemForm 
from django.contrib import messages
from .forms import ContactForm

User = get_user_model()
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
    
def archive_view(request):
    poems = Poem.objects.filter(is_published=True).order_by('-created_at')
    moods = MoodTag.objects.all()

    # Optional mood filter
    mood_name = request.GET.get('mood')
    if mood_name:
        poems = poems.filter(mood__name=mood_name)

    context = {
        'poems': poems,
        'moods': moods
    }

    return render(request, 'archive.html', context)


def curations_view(request):
    featured_poems = Poem.objects.filter(is_featured=True, is_published=True)
    return render(request, 'curations.html', {'featured_poems': featured_poems})


from .models import Poet

def poets_view(request):
    poets = Poet.objects.all()
    return render(request, 'poets.html', {'poets': poets})


def journal_view(request):
    poems = Poem.objects.filter(is_published=True).order_by('-created_at')[:10]
    return render(request, 'journal.html', {'poems': poems})


def about_view(request):
    return render(request, 'about.html')


def philosophy_view(request):
    return render(request, 'philosophy.html')


def privacy_view(request):
    return render(request, 'privacy.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Optional: send email (safe fallback if email not configured)
            if hasattr(settings, 'EMAIL_HOST'):
                send_mail(
                    subject=f'Poems With AD Contact: {name}',
                    message=message,
                    from_email=email,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],
                    fail_silently=True,
                )

            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

@login_required
def submit_poem_view(request):
    if request.method == "POST":
        form = PoemForm(request.POST, request.FILES)
        
        if form.is_valid():
            poem = form.save(commit=False)
            poem.author = request.user  # VERY IMPORTANT
            poem.save()

            messages.success(request, "Your verse has been submitted ✨")

            return redirect('poem_detail', slug=poem.slug)

    else:
        form = PoemForm()

    return render(request, 'submit.html', {
        'form': form
    })