# Register your models here.
from django.contrib import admin

"""
from .DataBaseModels.AddressdatamodelFile import Addressdatamodel
from .DataBaseModels.ClassdatamodelFile import Classdatamodel
from .DataBaseModels.SchooldatamodelFile import Schooldatamodel
from .DataBaseModels.StaffdatamodelFile import Staffdatamodel
from .DataBaseModels.StudentdatamodelFile import Studentdatamodel
"""
# from .DataBaseModels.SubjectdatamodelFile import Subjectdatamodel
"""


@admin.register(Schooldatamodel)
class SchooldataAdmin(admin.ModelAdmin):
    display = ('School_Name', 'School_Email')  # Display these fields in the list view


@admin.register(Staffdatamodel)
class StaffdataAdmin(admin.ModelAdmin):
    display = 'Staff_Name'


@admin.register(Studentdatamodel)
class Studentdataadmin(admin.ModelAdmin):
    display = 'Student_Firstname'


@admin.register(Classdatamodel)
class ClassAdmin(admin.ModelAdmin):
    display = 'ClassName'


@admin.register(Subjectdatamodel)
class SubjectAdmin(admin.ModelAdmin):
    display = 'Subjects'


@admin.register(Addressdatamodel)
class SubjectAdmin(admin.ModelAdmin):
    display = 'State'
"""
