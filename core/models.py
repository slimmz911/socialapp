from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # to remove all the activities of a deleted user 
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='avatar.jpeg')
    location = models.CharField(max_length=80)


    def __str__(self):
        return self.user.username