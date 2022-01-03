from django.contrib import admin
from .models import Student, AvailableCourse, Registration

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(AvailableCourse)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['nam']


@admin.register(Registration)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name']
