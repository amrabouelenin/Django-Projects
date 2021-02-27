from django.db import models

# Employee Entity
class EmployeeEntity(models.Model):
    # entitty name
    entity_name = models.CharField(max_length=256, null=False, unique = True, verbose_name = 'Entity Name')
    # unique entity code
    entity_code = models.CharField(unique= True, null = False, max_length=256, verbose_name = 'Entity Code')
