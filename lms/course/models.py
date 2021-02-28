from django.db import models
from djrichtextfield.models import RichTextField


# category of the course
class Category(models.Model):
    # Name of category
    name = models.CharField(max_length=255, unique= True, help_text = "Category")
    def __str__(self):
        return self.name

# Target Audience of the course
class TargetAudience(models.Model):

    # Name of category
    name = models.CharField(max_length=255, unique= True, help_text = "Target Audience")

    def __str__(self):
        return self.name




# Main course model
class Course(models.Model):
    course_name = models.CharField(unique=True, max_length=255, verbose_name = "Course Name")
    course_overview = RichTextField(help_text = "Write an overview about the course", verbose_name = 'Overview')
    course_objective = RichTextField(help_text = "Write the objective of the course", verbose_name = 'Objective')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.DO_NOTHING)
    target_audience = models.ForeignKey(TargetAudience, null=True, blank=True, on_delete=models.DO_NOTHING)
    prerequisites = RichTextField(help_text = "Write the Prerequisites of the course", verbose_name = 'Prerequisites')
    course_img = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, help_text = 'make it clean and neat. ;) ')
    prerequisites_courses = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING)





