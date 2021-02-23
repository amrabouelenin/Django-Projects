from django import forms
from smartcity_app import models


class BeaconFrom(forms.ModelForm):
    class Meta:
        fields = {'beacon_id', 'location', 'vehicle_id'}
        model = models.Beacon

