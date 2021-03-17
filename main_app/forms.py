from django import forms
from .models import User 

class UsernameForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username']