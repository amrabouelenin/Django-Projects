from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from customuser_app.models import User
from customuser_app.forms import UserCreationForm, UserChangeForm
# Alter UserAdmin Form
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'profile_pic','username',  'dob')
    list_filter = ('favorite_color',)
    fieldsets = (
        (None, {'fields': ('email', )}),
        ('Personal info', {'fields': ('dob', 'profile_pic')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'profile_pic', 'dob', 'password1', 'password2'),
        }),
    )
    #search_fields = ('email',)
    #ordering = ('email',)
    #filter_horizontal = ()


# Register your models here.
admin.site.register(User, UserAdmin)
