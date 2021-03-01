from django.db import models
from djrichtextfield.models import RichTextField
import datetime
from django_fsm import FSMField, transition
from django.utils import timezone

# category of the course
class Category(models.Model):
    # Name of category
    name = models.CharField(max_length=255, unique= True, help_text = "Category")
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

# Target Audience of the course
class TargetAudience(models.Model):

    # Name of category
    name = models.CharField(max_length=255, unique= True, help_text = "Target Audience")

    def __str__(self):
        return self.name


# Location
class Location(models.Model):
    # Location
    location_name = models.CharField(unique=True, max_length=255, verbose_name = "Location")
    
# Vendor
class Vendor(models.Model):
    #Vendor
    vendor_name = models.CharField(unique=True, max_length=255, verbose_name= 'Vendor Name')

# Main course model
class Course(models.Model):

    # Course Name
    course_name = models.CharField(unique=True, max_length=255, verbose_name = "Course Name")
    
    # Overview
    course_overview = RichTextField(help_text = "Write an overview about the course", verbose_name = 'Overview')
    
    # Objective
    course_objective = RichTextField(help_text = "Write the objective of the course", verbose_name = 'Objective')
    
    # Category
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.DO_NOTHING)
    
    # Target audience of the course
    target_audience = models.ForeignKey(TargetAudience, null=True, blank=True, on_delete=models.DO_NOTHING)
    
    # Prerequisites
    prerequisites = RichTextField(help_text = "Write the Prerequisites of the course", verbose_name = 'Prerequisites')
    
    # Main image for the course to appear in the main view
    course_img = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, help_text = 'make it clean and neat. ;) ')

    # self reference to courses
    prerequisites_courses = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING)
    
    # Certification
    course_certification = RichTextField(default='Course Certification',help_text = "Write the course certification", verbose_name = 'Certification')

    # Lis of years - choices +5, -5 current year
    Years = []
    start_year = datetime.datetime.now().year - 5
    for i in range(10):
        start_year += 1
        Years.append((start_year,start_year))

    # year the user has been added
    year = models.IntegerField(choices=Years, default=start_year-5)

# Workflow State for Course Schedule
class ScheduleState(object):
 
    '''
    Constants to represent the `state`s of the Course Schedule
    '''
    ACCEPTING_NOMINATIONS = 'accepting_nominations'            # Course is accepting nominationn
    REGISTERATION_CLOSED = 'registeration_closed'              # Rigesteration closed
    STARTED = 'started'                                        # Course Started
    END_BATCH = 'end_batch'                                    # course batch has been ended

    CHOICES = (
        (ACCEPTING_NOMINATIONS, 'Accepting Nominiations'),
        (REGISTERATION_CLOSED, 'Registeration Closed'),
        (STARTED, 'Started'),
        (END_BATCH, 'End Batch'),
    )



# Course Schedule
class CourseSchedule(models.Model):

    # reference to courses
    course_name = models.ForeignKey(Course, null=False, on_delete=models.DO_NOTHING)
    
    # E-Learning Classes
    E_CLASS = 'EC'
    # Face to Face Classes
    F_F_CLASS = 'FFC'
    #Blineded Classes
    B_CLASS = 'BC'
    # course delivery methods
    Methods = [
            (E_CLASS, 'E-Learning Classes'),
            (F_F_CLASS, 'Face To Face Classes'),
            (B_CLASS, 'Blinded Classes'),
    ]

    delivery_method = models.CharField(max_length=256, choices=Methods, default=E_CLASS, verbose_name='Course delivery method')
    
    # Location of the course
    location = models.ForeignKey(Location, null=True, on_delete=models.DO_NOTHING)
    
    # Vendor 
    vendor = models.ForeignKey(Vendor, null=True, on_delete=models.DO_NOTHING)

    # schedule state WORKFLOW
    schedule_state = FSMField( default=ScheduleState.ACCEPTING_NOMINATIONS,verbose_name='Schedule Status',choices=ScheduleState.CHOICES,protected=False,)


    # start date
    start_date    = models.DateField(default = timezone.now,auto_now=False, verbose_name = 'Start Date', auto_now_add=False, help_text = "Please write the start date of this batch")
    
    # end date
    end_date    = models.DateField(default =timezone.now, auto_now=False, verbose_name='End Date', auto_now_add=False, help_text = "Please write the start date of this batch")


# Session of the course
class Session(models.Model):
   
    # session date
    session_date    = models.DateField(auto_now=False, verbose_name='Session Date', auto_now_add=False, help_text = "Please write the start date of this batch")
    
    # start time
    start_time    = models.TimeField(auto_now=False, verbose_name='Start time', auto_now_add=False, help_text = "Session start time")
    
    # end time
    end_time    = models.TimeField(auto_now=False, verbose_name='End time', auto_now_add=False, help_text = "Session end time")

    # reference to course schedule and allow multiple sessions
    course_schedule = models.ForeignKey(CourseSchedule, on_delete=models.DO_NOTHING,null=False)

# Instructor Model
class Instructor(models.Model):
   
    # Name of instructor
    instructor_name = models.CharField(unique=True, max_length=255, verbose_name= 'Instructor Name')
    
    # mutliple instructors can be linked with one schedule
    course_schedule = models.ForeignKey(CourseSchedule, null=True, on_delete=models.DO_NOTHING, verbose_name = 'Linked Course Schedule')


