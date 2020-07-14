from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url=reverse_lazy('home')
    model=CustomUser
    template_name='signup.html'



# Create your views here.
