from django.urls import path
from . import views
from .views import create_post, edit_post, delete_post


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('post/create/', create_post, name='create_post'),
    path('post/edit/<int:post_id>/', edit_post, name='edit_post'),
    path('post/delete/<int:post_id>/', delete_post, name='delete_post'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
