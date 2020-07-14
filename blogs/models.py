from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Blog(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])

# Create your models here.
