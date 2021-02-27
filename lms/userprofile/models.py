from django.db import models
from django.contrib.auth.models import AbstractUser

from itp.models import JobRole
from emp_entity.models import EmployeeEntity
from django_countries.fields import CountryField
class User(AbstractUser):
    username = models.CharField(unique=True,max_length=150, verbose_name = 'Login Id')

# Custom user profile to extend default user model
class UserProfile(models.Model):

    # Link to default user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # reference to Standard ITP Job Role
    Job_role = models.ForeignKey(JobRole, default = 1, null = False, on_delete = models.DO_NOTHING, verbose_name= 'Standard ITP Role', related_name = 'profile_jobrole')

    # reference to Employee Entity
    entity_name = models.ForeignKey(EmployeeEntity, default = 1, null = False, on_delete = models.DO_NOTHING, verbose_name= 'Entity Name', related_name = 'profile_entity')
    
    # Nationality shall read from country field
    nationality = CountryField(default= 1, null = False, blank_label='(select country)')


