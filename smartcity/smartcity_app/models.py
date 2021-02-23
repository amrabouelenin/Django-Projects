from django.db import models
from geolocation_fields.models import fields
from django.conf import settings
from django.urls import reverse
# Create your models here.



# Vehicle
class Vehicle(models.Model):

    vehicle_id = models.CharField(max_length=256,primary_key= True)

# Beacon Model
class Beacon(models.Model):
 
    beacon_id = models.AutoField(primary_key=True)
    location = fields.PointField(verbose_name = 'location', max_length=256)
    vehicle_id = models.ForeignKey(Vehicle, null=False, on_delete= models.DO_NOTHING, default=1)

    def get_absolute_url(self):
        return reverse(
            "smartcity_app:beacons",
        )


# Station Model
class Station(models.Model):

    station_name = models.CharField(max_length=256, null=False, help_text='Please write the station name i.e Lodz Fabrycna')
    station_id = models.AutoField(null = False, primary_key=True)
    location = fields.PointField(verbose_name= 'location', null= False, help_text='Please drag the mouse to the location of the station')
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['station_name'], name='unique_station_name'),
        ]

    def get_absolute_url(self):
        return reverse(
            "smartcity_app:stations",
        )



# Trip Model
class Trip(models.Model):
    from_station = models.ForeignKey(Station, null = False, on_delete=models.DO_NOTHING, related_name = 'from_station')
    to_station = models.ForeignKey(Station, null = False, on_delete=models.DO_NOTHING, related_name = 'to_station')
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, limit_choices_to= {'groups__name': 'passenger'})

    def get_absolute_url(self):
        return reverse(
            "smartcity_app:trips",
        )


