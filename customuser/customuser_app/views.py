from django.shortcuts import render
from customuser_app.forms import UserCreationForm
from django.views.generic import CreateView
from customuser_app import forms
from django.urls import reverse_lazy, reverse

# Create your views here.

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreationForm
    template_name = "add_user.html"

    def get_success_url(self):
        #messages.add_message(self.request, messages.INFO, 'Passenger has been added successfully')
        return reverse('customuser_app:add_passenger')

