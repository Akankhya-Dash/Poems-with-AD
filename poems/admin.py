from django.contrib import admin
from .models import Poem, MoodTag


@admin.register(MoodTag)
class MoodTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'intensity')
    search_fields = ('name',)


@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'mood', 'is_published', 'is_featured')
    list_filter = ('is_published', 'is_featured', 'mood')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}