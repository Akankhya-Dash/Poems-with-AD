from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home_view, name='home'), 
    path('submit/', views.submit_poem_view, name='submit'),
    path('archive/', views.archive_view, name='archive'),
    path('curations/', views.curations_view, name='curations'),
    path('poets/', views.poets_view, name='poets'),
    path('journal/', views.journal_view, name='journal'),
    path('about/', views.about_view, name='about'),
    path('philosophy/', views.philosophy_view, name='philosophy'),
    path('privacy/', views.privacy_view, name='privacy'),
    path('contact/', views.contact_view, name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)