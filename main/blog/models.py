from django.utils import timezone
from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length = 100)
    subtitle = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
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
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    

    class Meta:
        ordering = ['created_on']


    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
    
    


    

