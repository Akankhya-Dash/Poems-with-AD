from django.shortcuts import render, get_object_or_404
from .models import Poem


def poem_detail(request, slug):
    poem = get_object_or_404(Poem, slug=slug, is_published=True)
    return render(request, 'poem_detail.html', {'poem': poem})