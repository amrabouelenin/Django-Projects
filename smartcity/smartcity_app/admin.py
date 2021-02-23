from django.contrib import admin
from smartcity_app.models import Beacon, Vehicle, Station, Trip
# Register your models here.
admin.site.register(Beacon)
admin.site.register(Vehicle)
admin.site.register(Station)
admin.site.register(Trip)
