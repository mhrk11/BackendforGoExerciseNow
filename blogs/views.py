
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Blog


class BlogCreateView(LoginRequiredMixin, CreateView):
    model=Blog
    template_name='blog_new.html'
    fields=['title', 'body']
    login_url='login'

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class BlogDetailView(LoginRequiredMixin, DetailView):
    model=Blog
    template_name='blog_detail.html'
    login_url='login'

class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name='blog_list.html'
    context_object_name='blogs_list'
    login_url='login'

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Blog
    template_name='blog_update.html'
    fields=['title', 'body']
    login_url='login'

    def test_func(self):
        obj=self.get_object()
        return obj.author==self.request.user

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Blog
    template_name='blog_delete.html'
    success_url=reverse_lazy('home')
    login_url='login'

    def test_func(self):
        obj=self.get_object()
        return obj.author==self.request.user




# Create your views here.
