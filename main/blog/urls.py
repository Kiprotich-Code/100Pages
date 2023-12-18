from django.urls import path
from . import views

urlpatterns = [
    # Urls for the Posts model 
    path('posts/', views.post_list, name="posts"),
    path('add_post/', views.add_posts, name="add_post"),
    path('post_detail/ <id>', views.post_detail, name="post_detail"),
    path('upvote_post/ <id>', views.upvote_post, name="upvote_post"),
    path('downvote_post/ <id>', views.downvote_post, name="downvote_post"),
]