from django.db import models
from userprofile.models import User # new
from django_fsm import FSMField, transition
from course.models import CourseSchedule
# Create your models here.


# Attendance Model
class Attendance(models.Model):

    # Upload the sheet of attendance
    attendance_sheet= models.FileField(upload_to='uploads/')
    
    # Status of attendance
    ABSENT = 'absent'
    PRESENT = 'present'
    INCOMPLETE = 'incomplete'
    STATUS = [
        (ABSENT, 'Absent'),
        (PRESENT, 'Present'),
        (INCOMPLETE, 'Incomplete'),
    ]
    # attendance status
    attendance_status = models.CharField(max_length=120,choices=STATUS, default=ABSENT)

    # reference to course schedule and allow multiple sessions
    course_schedule = models.ForeignKey(CourseSchedule, on_delete=models.DO_NOTHING,null=False)
    
    # Trainee - reference to user
    trainee = models.ForeignKey(User, on_delete=models.CASCADE) 
 
