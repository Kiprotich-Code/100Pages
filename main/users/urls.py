from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),

    # Profile 
    path('profile/', views.profile, name='profile'),
    path('view_profile/<int:id>/', views.view_profile,  name='view_profile' ),
    path('author_profile/<int:user_id>/', views.author_profile,  name='author_profile' ),
    path('profile_posts/<user_id>/', views.profile_posts,  name='profile_posts' ),
    path('profile_upvotes/<int:id>', views.profile_upvotes,  name='profile_upvotes' ),
    path('profile_downvotes/<int:id>/', views.profile_downvotes,  name='profile_downvotes' ),
]
