from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from braces.views import SelectRelatedMixin
from accounts.models import User
from smartcity_app.models import Trip, Station


class DashboardPage(TemplateView):
    template_name = 'dashboard.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users_count'] = User.objects.count() 
        context['trips_count'] = Trip.objects.count() 
        context['stations_count'] = Station.objects.count() 
        return context

# Create your views here.
class HomePage(TemplateView):
    template_name = "login.html"

# Trips
class Trips(generic.ListView):
    model = models.Trip
    template_name = "trips.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# Beacons
class Beacons(generic.ListView):
    model =models.Beacon
    template_name = 'beacons.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# Stations
class Stations(generic.ListView):
    model = models.Station
    template_name = 'stations.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# Stations
class Vehicles(generic.ListView):
    model = models.Vehicle
    template_name = 'vehicles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


## Creation Forms

# Create Beacon
class CreateBeacon(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
        
    fields = {'beacon_id', 'location', 'vehicle_id'}
    model = models.Beacon

# Create Station
class CreateStation(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
        
    fields = {'station_name', 'station_id', 'location'}
    model = models.Station

# Create Trip
class CreateTrip(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
        
    fields = {'from_station', 'to_station', 'passenger'}
    model = models.Trip

