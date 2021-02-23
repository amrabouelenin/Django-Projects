from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
#from accounts.models import User

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username','profile_pic',  'email', 'password1', 'password2')
        model = get_user_model()



# User Change/Update Form
class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    class Meta:
        model = get_user_model()
        fields = ( 'username', 'email', 'profile_pic')
