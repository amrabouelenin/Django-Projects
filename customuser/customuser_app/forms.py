from customuser_app.models import User
from django import forms

# User Creation Form
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput) 
    class Meta:
        model = User
        fields = ( 'username', 'email', 'profile_pic', 'favorite_color')


# User Change/Update Form
class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    class Meta:
        model = User
        fields = ( 'username', 'email', 'profile_pic', 'dob', 'favorite_color')
