from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.urls import path
from . import views
# from .forms import PostForm
from .models import Post, Location, User
from .forms import UsernameForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


@login_required
def profile(request):
    locations = Location.objects.all()
    return render(request, 'profile.html', { 'locations': locations })

@login_required
def posts_detail(request, post_id):
  posts = Post.objects.get(id=post_id)
  return render(request, 'profile/detail.html', { 'posts': posts })

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

@login_required
def post_new(request):
  post_form = PostForm(request.POST or None)
  if request.POST and post_form.is_valid():
    new_post = post_form.save(commit=False)
    new_post.user = request.user
    new_post.save()
    # redirect to index
    return redirect('index')
  else:
    return render(request, 'posts/new.html', { 'post_form': post_form })

@login_required
def add_post(request, post_id):
    form = PostForm(request.POST)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.post_id = post_id
        new_post.save()
    return redirect('detail', post_id=post_id)

@login_required
def profile_edit(request, user_id):
  user = User.objects.get(id=user_id)
  username_form = UsernameForm(request.POST or None, instance=user)
  if request.POST and username_form.is_valid():
    username_form.save()
    # redirect to the detail page
    return redirect('profile')
  else:
    return render(request, 'profile/edit.html', { 'username_form': username_form, 'user_id': user_id })
