from django.contrib import admin
from Baseuser.models import BaseUser
from schools.models import School
from classes.models import Class
from subjects.models import Subject
from students.models import Student
from staffs.models import Staff



# Register your models here.
admin.site.register(BaseUser)
admin.site.register(School)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Staff)

# Customize the admin site
admin.site.site_header = 'School ERP'
admin.site.site_title = 'School ERP'
admin.site.index_title = 'Welcome to School ERP'
