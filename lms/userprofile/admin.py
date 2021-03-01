from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from userprofile.models import UserProfile, User, ITP

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'userprofile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

# Re-register UserAdmin
#admin.site.unregister(User)
admin.site.register(ITP)
admin.site.register(User, UserAdmin)
