from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    '''Custom User'''
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
