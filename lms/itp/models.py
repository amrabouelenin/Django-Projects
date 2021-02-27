from django.db import models

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
