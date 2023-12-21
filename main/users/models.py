from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dp = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    stage_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, blank=True)
    interests = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username}'
