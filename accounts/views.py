from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})




def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    next_url = request.GET.get('next', 'home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # This gets the user object
            user = form.get_user()
            # Log them in
            login(request, user)
            messages.success(request, f"Welcome back, {user.username} ✨")
            # REDIRECT to home
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from poems.models import Poem, User

from .models import Profile

@login_required
def profile_view(request):
    if request.user.is_superuser:
        return redirect('admin_dashboard')
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    poems = Poem.objects.filter(author=user).order_by('-created_at')[:5]
    poem_count = Poem.objects.filter(author=user).count()
    
    context = {
        'user': user,
        'profile': profile,
        'poems': poems,
        'poem_count': poem_count,
    }

    return render(request, 'profile.html', context)

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404

@staff_member_required
def admin_dashboard(request):
    users = User.objects.all()
    poems = Poem.objects.all()

    return render(request, 'admin_dashboard.html', {
        'users': users,
        'poems': poems
    })
    
@staff_member_required
def toggle_writer(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = user.profile

    profile.is_writer = not profile.is_writer
    profile.save()

    return redirect('admin_dashboard')

@staff_member_required
def toggle_writer(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = user.profile

    profile.is_writer = not profile.is_writer
    profile.save()

    return redirect('admin_dashboard')

@staff_member_required
def approve_poem(request, poem_id):
    poem = get_object_or_404(Poem, id=poem_id)
    poem.is_approved = True
    poem.is_published = True
    poem.save()

    return redirect('admin_dashboard')

@staff_member_required
def feature_poem(request, poem_id):
    poem = get_object_or_404(Poem, id=poem_id)
    poem.is_featured = not poem.is_featured
    poem.save()

    return redirect('admin_dashboard')


def is_admin(user):
    return user.is_superuser

from django.contrib.auth.decorators import user_passes_test
@user_passes_test(is_admin)
def admin_dashboard(request):
    users = User.objects.filter(is_staff=False)  # or custom filter
    poems = Poem.objects.all()

    context = {
        'users': users,
        'poems': poems
    }
    return render(request, 'admin_dashboard.html', context)