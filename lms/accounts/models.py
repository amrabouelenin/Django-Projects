from django.db import models
from django.contrib.auth.models import User
# Create user profile linked with default user model

class Account(models.Model):
    
    # link to default user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Non Auth fields
    # department
    department = models.CharField(max_length=256)

