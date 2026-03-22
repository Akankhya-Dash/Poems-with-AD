from django.urls import path
from .views import poem_detail

urlpatterns = [
    path('<slug:slug>/', poem_detail, name='poem_detail'),
]