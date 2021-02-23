from django.shortcuts import render
from django.contrib.auth import login, logout
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic.list import ListView
#from accounts.models import User
from . import forms
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    template_name = "accounts/add_passenger.html"

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Passenger has been added successfully')
        return reverse('accounts:add_passenger')

class UserListView(ListView):
    model = get_user_model()
    template_name = "accounts/user_list.html"
    #user_model = get_user_model
    paginate_by = 6  # if pagination is desired
    def get_context_data(self, **Kwargs):
        context = super().get_context_data(**Kwargs)
        context['now'] = timezone.now()
        #context['passengers'] = user_model.objects.all()
        return context
