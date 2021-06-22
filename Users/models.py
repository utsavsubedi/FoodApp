from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField( default = 'profile.jpg', upload_to = 'profile_pictures/' )
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}"