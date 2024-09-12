from django.urls import path
from .views import user_profile, delete_account, password_reset_view

urlpatterns = [
    path('profile/', user_profile, name='user_profile'),
    path('delete/', delete_account, name='delete_account'),
    path('password-reset/', password_reset_view, name='password_reset'),
]
