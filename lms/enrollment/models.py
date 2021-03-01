from django.db import models
from userprofile.models import User # new
from course.models import CourseSchedule
from django_fsm import FSMField, transition
# Create your models here.

# Workflow State for Enrollment
class EnrollementState(object):
 
    '''
    Constants to represent the `state`s of the Enrollement Status
    '''
    PENDING = 'pending'     
    UNDER_CONSIDERATION = 'under_consideration'     
    APPROVED = 'approved'                   
    REJECTED = 'rejected'                   

    CHOICES = (
        (PENDING, 'Pending'),
        (UNDER_CONSIDERATION, 'Under Consideration'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    )

# Nomination Model
class Nomination(models.Model):

    # reference to course schedule and allow multiple sessions
    course_schedule = models.ForeignKey(CourseSchedule, on_delete=models.DO_NOTHING,null=False)
    
     # Trainee - reference to user
    trainee = models.ForeignKey(User, on_delete=models.CASCADE) 
   
    # Enrollement Status - Workflow
    enrollement_state = FSMField( default=EnrollementState.PENDING,verbose_name='Enrollement Status',choices=EnrollementState.CHOICES,protected=False,)

