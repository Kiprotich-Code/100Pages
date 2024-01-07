from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dp = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    stage_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, blank=True)
    interests = models.CharField(max_length=100, blank=True)
    followers = models.ManyToManyField(User, related_name='followers', blank=True)

    def __str__(self):
        return f'{self.user.username}'
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.dp.path)
        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.dp.path)
