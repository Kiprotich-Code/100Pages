import os
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.title} by {self.author}'


class Comment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.commenter)


# Temporary model to check for users feedback 
class UserFeedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return f'Feedback from {self.name}'