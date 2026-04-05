from django.urls import path
from .views import approve_poem, feature_poem, signup_view, login_view, logout_view,profile_view,admin_dashboard, toggle_writer

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('toggle-writer/<int:user_id>/', toggle_writer, name='toggle_writer'),
    path('approve-poem/<int:poem_id>/', approve_poem, name='approve_poem'),
    path('feature-poem/<int:poem_id>/', feature_poem, name='feature_poem'),
]

from django.contrib.auth import views as auth_views

urlpatterns += [
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='forgot_password.html'
    ), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),
]