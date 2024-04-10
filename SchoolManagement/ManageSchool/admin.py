from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Schooldatamodel, Staffdatamodel, Studentdatamodel


@admin.register(Schooldatamodel)
class SchooldataAdmin(admin.ModelAdmin):
    list_display = ('School_Name', 'School_Email')  # Display these fields in the list view
    search_fields = ('School_Name', 'School_Name') # Enable search by username and email


@admin.register(Staffdatamodel)
class StaffdataAdmin(admin.ModelAdmin):
    list_display = ('Staff_Firstname', 'Staff_Lastname')
    search_fields = ('Staff_Firstname', 'Staff_ID')


@admin.register(Studentdatamodel)
class Studentdataadmin(admin.ModelAdmin):
    list_display = ('Student_Firstname', 'Student_Contact')
    search_fields = ('Student_Id', 'Student_Firstname')

# Register the model with the customized admin class
