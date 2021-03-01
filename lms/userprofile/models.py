from django.db import models
from django.contrib.auth.models import AbstractUser

from django_fsm import FSMField, transition
from itp.models import JobRole, Department
from emp_entity.models import EmployeeEntity
from django_countries.fields import CountryField

from phonenumber_field.modelfields import PhoneNumberField
import datetime

# Inherit default user model
class User(AbstractUser):
    username = models.CharField(unique=True,max_length=150, verbose_name = 'Login Id')

    class Meta:
        verbose_name= 'User Profile'
        verbose_name_plural = 'User Profiles'

# Custom user profile to extend default user model
class UserProfile(models.Model):
  
    # Lis of years - choices +5, -5 current year
    Years = []
    start_year = datetime.datetime.now().year - 5
    for i in range(10):
        start_year += 1
        Years.append((start_year,start_year))
   
    # Link to default user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # reference to Standard ITP Job Role
    Job_role = models.ForeignKey(JobRole, default = 1, null = False, on_delete = models.DO_NOTHING, verbose_name= 'Standard ITP Role', related_name = 'profile_jobrole')

    # reference to Employee Entity
    entity_name = models.ForeignKey(EmployeeEntity, default = 1, null = False, on_delete = models.DO_NOTHING, verbose_name= 'Entity Name', related_name = 'profile_entity')
    
    # Nationality shall read from country field
    nationality = CountryField(default= 1, null = False, blank_label='(select country)')
    
    # Mobile number
    phone_number = PhoneNumberField(default='+48691971923', verbose_name= 'Phone Number')
    
    # year the user has been added
    year = models.IntegerField(choices=Years, default=start_year-5)

    # Verified
    verified = models.IntegerField(choices = [(0, 'Not Verified'),(1, 'Verified')], default =0, help_text = 'please check this if you have verfieid the user')


# Workflow State for ITP
class ITPState(object):
 
    '''
    Constants to represent the `state`s of the ITP
    '''
    DRAFT = 'draft'            # Draft
    SUBMITTED = 'submitted'              # Subitted

    CHOICES = (
        (DRAFT, 'draft'),
        (SUBMITTED, 'Submitted'),
    )


class ITP(models.Model):
    # Lis of years - choices +5, -5 current year
    Years = []
    start_year = datetime.datetime.now().year - 5
    for i in range(10):
        start_year += 1
        Years.append((start_year,start_year))

    # year the user has been added
    year = models.IntegerField(choices=Years, verbose_name='ITP year',default=start_year-5)


    # Trainee - reference to user
    trainee = models.ForeignKey(User, on_delete=models.CASCADE)

    # Job Role reference
    job_role = models.ForeignKey(JobRole, on_delete=models.DO_NOTHING)
   
   # Department
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    
    # ITP Workflow Status
    itp_state = FSMField( default=ITPState.DRAFT,verbose_name='ITP Submission Status',choices=ITPState.CHOICES,protected=False,)


    





