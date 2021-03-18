from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('post/new/', views.post_new, name='new'),
    path('accounts/signup/', views.signup, name='signup'),
    path('post/<int:post_id>/add_post/', views.add_post, name="add_post"),
    path('profile/<int:user_id>/edit/', views.profile_edit, name="edit"),
    path('post/<int:post_id>/', views.posts_detail, name='detail'),
    
]
