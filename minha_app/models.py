from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
  pass

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description or 'Image uploaded by ' + self.user.username
