from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='images/', height_field = None, width_field=None, max_length=100, null= True) 
    dob = models.DateField(null = True)
    favorite_color = models.CharField(max_length=32, default='Blue')

# Create your models here.
