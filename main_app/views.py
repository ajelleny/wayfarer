from django.shortcuts import render, redirect
from django.urls import path
from . import views 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# from .forms import PostForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
          user = form.save()
          login(request, user)
          return redirect('profile')
        else:
          error_message = 'Invalid sign up - please try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# def posts_new(request):
#   post_form = PostForm(request.POST or None)
#   if request.POST and post_form.is_valid():
#     new_post = post_form.save(commit=False)
#     new_post.user = request.user
#     new_post.save()
#     # redirect to index
#     return redirect('index')
#   else:
#     return render(request, 'posts/new.html', { 'post_form': post_form }) 

