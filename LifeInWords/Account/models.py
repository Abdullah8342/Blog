'''Extending User Model'''
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    '''CustomUser Model'''
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
