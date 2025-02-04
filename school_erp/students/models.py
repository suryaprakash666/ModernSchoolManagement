from django.db import models
from Baseuser.models import BaseUser

class Student(BaseUser):
    roll_number = models.IntegerField(primary_key=True)
    standard = models.IntegerField(choices=[(1, '1st'), (2, '2nd'), (3, '3rd'), (4, '4th'), (5, '5th'), (6, '6th'), (7, '7th'), (8, '8th'), (9, '9th'), (10, '10th'), (11, '11th'), (12, '12th')])
    section = models.CharField(max_length=5, null=True, blank=True)
    school = models.ForeignKey('schools.School', on_delete=models.CASCADE)

    # Parents details
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    father_phone = models.CharField(max_length=15)
    mother_phone = models.CharField(max_length=15)
    class_teacher = models.ForeignKey('staffs.Staff', on_delete=models.CASCADE, related_name='students')

    # Address
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.IntegerField()


    #documents
    adharcard = models.FileField(upload_to='documents/adharcard/', null=True, blank=True)
    tc = models.FileField(upload_to='documents/tc/', null=True, blank=True)
    passportphoto = models.ImageField(upload_to='documents/passportphoto/', null=True, blank=True)

    #course
    #course = models.ManyToManyField('courses.Course', related_name='students')


    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        db_table = 'students'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class StudentRegistration(models.Model):
    school = models.ForeignKey('schools.School', on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.IntegerField()

    #documents
    adharcard = models.FileField(upload_to='registration_documents/adharcard/', null=True, blank=True)
    tc = models.FileField(upload_to='registration_documents/tc/', null=True, blank=True)
    passportphoto = models.ImageField(upload_to='registration_documents/passportphoto/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    #request status
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')

    class Meta:
        verbose_name = 'Student Registration'
        verbose_name_plural = 'Student Registrations'
        db_table = 'student_registrations'

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    