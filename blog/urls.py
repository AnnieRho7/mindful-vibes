from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.PostList.as_view(), name='blog'),
    #     path('', views.PostList.as_view(), name='home'),
    #     path('blog/', views.PostList.as_view(), name='blog'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
