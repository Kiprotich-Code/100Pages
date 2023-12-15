from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length = 100)
    subtitle = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    post = models.TextField()

    def __str__(self):
        return f'{self.title} by {self.author}'
    

