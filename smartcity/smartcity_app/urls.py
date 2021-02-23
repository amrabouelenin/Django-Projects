from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from smartcity_app.views import Trips,Stations,Beacons, Vehicles, CreateBeacon, CreateStation, CreateTrip

app_name = 'smartcity_app'

urlpatterns = [
    path('trips/',Trips.as_view(), name='trips'),
    path('beacons/',Beacons.as_view(), name='beacons'),
    path('stations/',Stations.as_view(), name='stations'),
    path('vehicles/',Vehicles.as_view(), name='vehicles'),
    path('vehicles/',Vehicles.as_view(), name='vehicles'),
    path('create/beacon/', CreateBeacon.as_view(), name="create_beacon"),
    path('create/station/', CreateStation.as_view(), name="create_station"),
    path('create/trip/', CreateTrip.as_view(), name="create_trip"),
]
