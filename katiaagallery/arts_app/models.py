from django.db import models
from djrichtextfield.models import RichTextField


# Model to create arts
class Art(models.Model):
    
    # Title of the art
    title   = models.CharField(max_length=264, unique= True, help_text = "Write an attractive title!")
    # Image for the art
    art_img = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, help_text = 'make it clean and neat. ;) ')
    # story behind that art
    story   = models.TextField(help_text = "Write an interesting story behind this art!")
    # When did you make this art
    date    = models.DateField(auto_now=False, auto_now_add=False, help_text = "Do you remember when you made this art ?")
    
    # reference to category field
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.DO_NOTHING)


# Model for About 
class About(models.Model):

    # title of about page
    title = models.CharField(max_length=264, unique= True, help_text = "write the title of this page!")

    # body of the page
    body = RichTextField(help_text = "Write an interesting text about you here")


# Model for Category
class Category(models.Model):

    # Name of category
    name = models.CharField(max_length=264, unique= True, help_text = "Category Name")

    # Description of Category
    discription = models.TextField(help_text = "Write an interesting text about you here", blank=True)


    def __str__(self):
        return self.name
