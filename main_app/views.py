from django.shortcuts import render, redirect
from django.urls import path
from . import views

# Create your views here.
def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')
