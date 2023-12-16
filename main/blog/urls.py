from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    # Urls for the Posts model 
    path('posts/', views.post_list, name="posts"),
    path('add_post/', views.add_posts, name="add_post"),
    path('post_detail/ <int:id>', views.post_detail, name="post_detail"),
]