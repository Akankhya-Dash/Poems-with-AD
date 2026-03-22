from django.urls import path
from .views import submit_poem

urlpatterns = [
    path('submit/', submit_poem, name='submit_poem'),
]