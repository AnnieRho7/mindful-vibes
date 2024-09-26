from django.urls import path
from django.contrib.auth import views as auth_views
from .views import user_profile, delete_account, view_user_profile

urlpatterns = [
    path(
        'profile/',
        user_profile,
        name='user_profile'
    ),
    path(
        'delete/',
        delete_account,
        name='delete_account'
    ),
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='account/password_reset.html'
        ),
        name='password_reset'
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='account/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='account/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='account/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
    path(
        'profile/<str:username>/',
        view_user_profile,
        name='view_user_profile'
    ),
]
