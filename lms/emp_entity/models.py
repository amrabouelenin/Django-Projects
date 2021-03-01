from django.db import models

# Employee Entity
class EmployeeEntity(models.Model):

    class Meta:
        verbose_name = 'Employee Entity'
        verbose_name_plural = 'Employee Entities'
    # entitty name
    entity_name = models.CharField(max_length=255, null=False, unique = True, verbose_name = 'Entity Name')
    # unique entity code
    entity_code = models.CharField(unique= True, null = False, max_length=150, verbose_name = 'Entity Code')
