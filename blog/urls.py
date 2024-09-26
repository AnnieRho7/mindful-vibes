from django.urls import path
from . import views
from .views import (
    create_post, edit_post, delete_post, user_profile_view,
    home, post_detail, comment_edit, comment_delete, subscribe
)
from .views import PostList

urlpatterns = [
    path('', home, name='home'),
    path('blog/', PostList.as_view(), name='blog'),
    path('post/create/', create_post, name='create_post'),
    path(
        'post/edit/<int:post_id>/',
        edit_post,
        name='edit_post'
    ),
    path(
        'post/delete/<int:post_id>/',
        delete_post,
        name='delete_post'
    ),
    path('subscribe/', subscribe, name='subscribe'),
    path(
        'user_profile/<str:username>/',
        user_profile_view,
        name='user_profile'
    ),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path(
        '<slug:slug>/edit_comment/<int:comment_id>/',
        comment_edit,
        name='comment_edit'
    ),
    path(
        '<slug:slug>/delete_comment/<int:comment_id>/',
        comment_delete,
        name='comment_delete'
    ),
]
