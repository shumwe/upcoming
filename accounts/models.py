from django.db import models
from django.contrib.auth.models import AbstractUser

def avatar_path(instance, filename):
    return "user-avatars/{0}/{1}".format(instance.username, filename)

class User(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatar', default='emt.png')
    
    def __str__(self):
        return f"{self.username}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=155, default="Kenya")
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    