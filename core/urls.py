from django.urls import path
from .views import home_view, mood_view

urlpatterns = [
    path('', home_view, name='home'),
    path('mood/<str:mood_name>/', mood_view, name='mood_filter'),
]