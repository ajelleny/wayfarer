from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('post/new/', views.post_new, name='new'),
    path('accounts/signup/', views.signup, name='signup')

]

