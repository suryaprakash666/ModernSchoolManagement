import uuid
from Baseuser.models import BaseUser
from django.db import models


class Staff(BaseUser):
    school = models.ForeignKey('schools.School', on_delete=models.CASCADE)
    designation = models.CharField(max_length=50, choices=[('Principal', 'Principal'), ('Teacher', 'Teacher'), ('Clerk', 'Clerk'), ('Peon', 'Peon')])
    department = models.CharField(max_length=50, choices=[('Science', 'Science'), ('Commerce', 'Commerce'), ('Arts', 'Arts'), ('Sports', 'Sports'), ('Music', 'Music')])
    salary = models.FloatField()

    # Address
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.IntegerField()

    #course
    #course = models.ManyToManyField('courses.Course', related_name='staffs')
    
    
    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staffs'
        db_table = 'staffs'
        
    def __str__(self):
        return self.first_name + ' ' + self.last_name