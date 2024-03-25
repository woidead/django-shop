from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)