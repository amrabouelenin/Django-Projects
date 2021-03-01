from django.db import models
#from userprofile.models import User
import datetime


# ITP required models

# Employee Department Model
class Department(models.Model):
    
    # Department Name
    dep_name = models.CharField(max_length = 256, verbose_name= 'Department Name')

# Employee Section Model
class Section(models.Model):

    # Section Name
    sec_name = models.CharField(max_length=256, verbose_name = 'Section Name')
    # reference department name
    dep_name = models.ForeignKey(Department, null = False, on_delete = models.DO_NOTHING, related_name = 'sec_dep')

# Employee Unit Model
class Unit(models.Model):

    # Unit Name
    unit_name = models.CharField(max_length=256, verbose_name = 'Unit Name')
    # reference section name
    sec_name = models.ForeignKey(Section, null = False, on_delete = models.DO_NOTHING, related_name = 'unit_sec')

# Employee Job Role
class JobRole(models.Model):

    # ITP Standard Job Role
    job_role = models.CharField(max_length=256, verbose_name = 'Standard ITP Role')
    # reference to unit name
    unit_name = models.ForeignKey(Unit, null = False, on_delete = models.DO_NOTHING, related_name = 'jobrole_unit')


class ITPCourse(models.Model):

    # Course Name
    course_name = models.CharField(unique=True, max_length=255, verbose_name = "Course Name")
   
    # Priority
    ESSENTIAL_REQUIRED = 'essential_required'
    REQUIRED_TRAINING = 'required_training'
    FUTURE_REQUIRED = 'future_reuired'
    FUTURE_DEVELOPMENT = 'future_development'
    PRIORITY_LIST = [
        (ESSENTIAL_REQUIRED, 'Essential Required'),
        (REQUIRED_TRAINING, 'Required Training'),
        (FUTURE_REQUIRED, 'Future Required'),
        (FUTURE_DEVELOPMENT, 'Future Development'),
    ]
    # priority
    priority= models.CharField(max_length=120,choices=PRIORITY_LIST, default=ESSENTIAL_REQUIRED)

 
    # Certificate Type
    PROFESSIONAL_CERTIFIED = 'professional_certified'
    PARTICIPANT_CERTIFIED = 'participant_certified'
    CERTFIEICATE_LIST = [
        (PROFESSIONAL_CERTIFIED, 'Professional Certified'),
        (PARTICIPANT_CERTIFIED, 'Participant Certfied'),
    ]
    # certificate type
    certificate_type= models.CharField(max_length=120,choices=CERTFIEICATE_LIST, default=PROFESSIONAL_CERTIFIED)
    remarks = models.TextField(blank = True)

    # link to itp


 
