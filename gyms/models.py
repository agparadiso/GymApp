from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

class Gym(models.Model):
    gym_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.gym_name

class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gym = models.ManyToManyField(Gym)
    
    def __str__(self):
        return self.user.username
