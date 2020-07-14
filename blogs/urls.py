from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailView, BlogDeleteView, BlogUpdateView

urlpatterns=[
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('new/', BlogCreateView.as_view(), name='blog_new'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('<int:pk>/edit/', BlogUpdateView.as_view(), name='blog_update'),
    ]
