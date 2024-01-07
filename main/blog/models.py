from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpeg', upload_to='profile_pics/')
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


# class Upvote(models.Model):
#     post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='upvotes')
#     upvoter = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=True)

#     class Meta:
#         ordering = ['created_on']

#     def __str__(self):
#         return self.upvoter