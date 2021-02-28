from django.contrib import admin
from course.models import Course, Category, TargetAudience

# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(TargetAudience)
