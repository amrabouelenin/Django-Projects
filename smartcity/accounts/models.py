from django.contrib import auth
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    profile_pic = models.ImageField(default = '', upload_to='images/', height_field=None,null = True, width_field=None, max_length=100, help_text = 'make it clean and neat. ;) ')
    def __str__(self):
       return "@{}".format(self.username)
#
