from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields=['email', 'username', 'age']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=['email', 'username', 'age']
