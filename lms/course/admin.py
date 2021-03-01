from django.contrib import admin
from course.models import Course, Category, TargetAudience, CourseSchedule, Vendor, Location, Instructor, Session

# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(TargetAudience)
admin.site.register(CourseSchedule)
admin.site.register(Location)
admin.site.register(Vendor)
admin.site.register(Instructor)
admin.site.register(Session)
