from django.db import models
from django.contrib.auth.models import User

class Gym(models.Model):
    gym_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.gym_name

class GymAdministrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username